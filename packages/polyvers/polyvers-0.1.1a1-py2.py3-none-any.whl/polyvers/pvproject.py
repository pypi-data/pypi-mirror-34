#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2015-2018 European Commission (JRC);
# Licensed under the EUPL 1.2+ (the 'Licence');
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at: http://ec.europa.eu/idabc/eupl
#
"""
The main structures of *polyvers*::

    Project 1-->* Engrave 1-->* Graft
"""
from pathlib import Path
from typing import List, Optional, Match, Sequence, Union, Pattern
import logging
import re

import polyversion as pvlib
import textwrap as tw

from . import vermath
from ._vendor.traitlets import traitlets as trt
from ._vendor.traitlets.traitlets import (
    List as ListTrait, Set as SetTrait, Tuple as TupleTrait, Union as UnionTrait)
from ._vendor.traitlets.traitlets import Bool, Unicode, Instance
from .cmdlet import cmdlets, autotrait
from .cmdlet.slicetrait import Slice as SliceTrait
from .utils import yamlutil as yu
from .utils.oscmd import cmd


log = logging.getLogger(__name__)


PatternClass = type(re.compile('.*'))  # For traitlets
MatchClass = type(re.match('.*', ''))  # For traitlets

FPaths = List[Path]
FLike = Union[str, Path]
FLikeList = Sequence[FLike]


def _slices_to_ids(slices, thelist):
    from boltons.setutils import IndexedSet as iset

    all_ids = list(range(len(thelist)))
    mask_ids = iset()
    for aslice in slices:
        mask_ids.update(all_ids[aslice])

    return list(mask_ids)


class Graft(cmdlets.Replaceable, cmdlets.Printable, yu.YAMLable, cmdlets.Spec):
    """Instructions on how to search'n replace some text."""

    name = Unicode(
        config=True,
        help="Describe it for readable printouts.")

    regex: str = Unicode(  # type: ignore
        read_only=True,
        config=True,
        help="The regular-expressions to search within the byte-contents of files."
    )

    @trt.validate('regex')
    def _is_valid_regex(self, proposal):
        value = proposal.value
        try:
            v = self.interp(value,
                            _stub_keys=lambda k: '<%s>' % k,  # real values from project
                            _escaped_for='regex')
            re.compile(v.encode(self.encoding))
        except Exception as ex:
            proposal.trait.error(None, value, ex)
        return value

    def regex_resolved(self, project: 'Project') -> Pattern:
        v = project.interp(self.regex, _escaped_for='regex')
        assert v, (self.regex, project)
        return re.compile(v.encode(self.encoding))

    subst = Unicode(
        allow_none=True, default_value='',
        help="""
        What to replace with; if `None`, no substitution happens.

        Inside them, supported extensions are:
        - captured groups with '\\1 or '\g<foo>' expressions
          (see Python's regex documentation)
        - interpolation variables; Keys available (apart from env-vars prefixed with '$'):
          {ikeys}
        - WARN: put x2 all '{' and '}' chars like this: `\\w{{1,5}}` or else,
          interpolation will scream.
        """
    )

    def subst_resolved(self, project: 'Project') -> bytes:
        v = project.interp(self.subst)
        assert v, (self.subst, project)
        return v.encode(self.encoding)

    slices = UnionTrait(
        (SliceTrait(), ListTrait(SliceTrait())),
        read_only=True,
        config=True,
        help="""
        Which of the `hits` to substitute, in "slice" notation(s); all if not given.

        Example::

            gs = Graft()
            gs.slices = 0                ## Only the 1st match.
            gs.slices = '1:'             ## Everything except the 1st match
            gs.slices = ['1:3', '-1:']   ## Only 2nd, 3rd and the last match.
                "

        """
    )

    encoding = Unicode(
        'utf-8',
        config=True,
        help="""How to encode regex into bytes for matching file contents.""")

    def collect_matches(self, fbytes: bytes, project: 'Project') -> List[Match]:
        """
        :return:
            all `hits`; use :meth:`sliced_matches` to apply any slices
        """
        with self.errlogged(token='scan',
                            doing="scanning %s" % self):
            regex = self.regex_resolved(project)
            matches = list(regex.finditer(fbytes))

        return matches

    def sliced_matches(self, matches: List[Match]) -> List[Match]:
        slices = self.slices
        if not slices or not matches:
            return matches
        else:
            if not isinstance(slices, list):
                slices = [slices]

            match_indices = _slices_to_ids(slices, matches)
            return [matches[i] for i in match_indices]

    def __str__(self):
        if self.name:
            return '%s(%s)' % (type(self).__name__, self.name)
        return super().__str__()


class Engrave(cmdlets.Replaceable, cmdlets.Printable, yu.YAMLable, cmdlets.Spec):
    """Muliple file-patterns to search'n replace."""

    name = Unicode(
        config=True,
        help="""
        Describe it for readable printouts, and refer to it from `Project.active_engraves` list.
        """)

    globs = ListTrait(
        Unicode(),
        read_only=True,
        config=True,
        help="A list of POSIX file patterns (.gitgnore-like) to search and replace"
    ).tag(printable=True)

    grafts = ListTrait(
        autotrait.AutoInstance(Graft),
        read_only=True,
        config=True,
        help="""
        A list of `Graft` for engraving (search & replace) version-ids or other infos.

        Use `{appname} config desc Graft` to see its syntax.
        """
    )

    def __str__(self):
        if self.name:
            return '%s(%s)' % (type(self).__name__, self.name)
        return super().__str__()


class Project(cmdlets.Replaceable, cmdlets.Printable, yu.YAMLable, cmdlets.Spec):
    """Configurations for projects, in general, and specifically for each one."""
    pname = Unicode(
        config=True,
        help="""The name of the project, used in interpolations and pvtags, among others."""
    ).tag(printable=True)

    basepath = Instance(
        Path,
        default_value=None, allow_none=True,
        castable=str,
        config=True,
        help="""
        The root-dir of this project.

        - Usually this the folder where `setup.py` resides.
        - Projects may be nested but not exactly overlap.
        - Searched and substitutions for a project stop when reaching
          the basepath of other projects.
          """
    ).tag(printable=True)

    printable_traits = 'pname basepath'.split()

    start_version_id = Unicode(
        '0.0.0',
        config=True,
        help="""If no pvtag found, use this as the base for relative versions.""")

    current_version = vermath.Pep440Version(
        None, allow_none=True,
        help="The previous version, auto-discovered.")

    release_date = Unicode(
        help="The automatic release date, to interpolate it.")

    @trt.default('release_date')
    def _get_now(self):
        from datetime import datetime

        return datetime.now().isoformat()

    ## TODO: rename version-->new_version
    version = vermath.Pep440Version(
        None, allow_none=True,
        help="The new absolute version to bump to.")

    def load_current_version_from_history(self, vtag_index=0):
        try:
            tag = self.pvtags_history[vtag_index]
            self.current_version = self.version_from_pvtag(tag)
        except IndexError:
            self.log.debug("No vtags history for %s.", self)
            self.current_version = self.start_version_id

    def set_new_version(self, version_bump: str = None):
        """
        :param version_bump:
            relative or absolute
        """
        if not version_bump:
            version_bump = self.default_version_bump

        if vermath.is_version_id_relative(version_bump):
            self.version = vermath.add_versions(self.current_version, version_bump)
        else:
            self.version = version_bump

    tag_vprefixes = TupleTrait(
        Unicode(), Unicode(),
        default_value=pvlib.tag_vprefixes,
        config=True,
        help="""
        A 2-tuple containing the ``{vprefix}`` interpolation values,
        one for *version-tags* and one for *release-tags*, respectively.
    """)

    pvtag_format = Unicode(
        help="""
        The pattern to generate new *pvtags*.

        It is interpolated with this class's traits as :pep:`3101` parameters;
        among others ``{pname}`` and ``{version}``; use ``{ikeys}`` to receive
        all available keys.

        .. Important::
           If you change this, ensure the :func:`polyversion.polyversion()`
           gets invoked from project's sources with the same value
           in `pvtag_format` kw-arg.
    """).tag(config=True)

    def _format_vtag(self, version, is_release=False):
        return self.interp(self.pvtag_format,
                           version=version,
                           vprefix=self.tag_vprefixes[int(is_release)])

    def tag_fnmatch(self, is_release=False):
        """
        The glob-pattern finding *pvtags* with ``git describe --match <pattern>`` cmd.

        :param is_release:
            `False` for version-tags, `True` for release-tags

        By default, it is interpolated with two :pep:`3101` parameters::

            {pname}   <-- this Project.pname
            {version} <-- '*'
        """
        vprefix = self.tag_vprefixes[int(is_release)]
        return self.interp(self.pvtag_format,
                           vprefix=vprefix,
                           version='*',
                           _escaped_for='glob')

    pvtag_regex = Unicode(
        help="""
        The regex pattern breaking *pvtags* and/or ``git-describe`` output
        into 3 named capturing groups:
        - ``pname``,
        - ``version`` (without the 'v'),
        - ``descid`` (optional) anything following the dash('-') after
          the version in ``git-describe`` result.

        It is interpolated with this class's traits as :pep:`3101` parameters;
        among others ``{pname}``, and **maybe** ``{version}``; use ``{ikeys}``
        to receive all available keys.
        See :pep:`0426` for project-name characters and format.

        .. Important::
           If you change this, ensure the :func:`polyversion.polyversion()`
           gets invoked from project's sources with the same value
           in `pvtag_regex` kw-arg.
    """).tag(config=True)

    @trt.validate('pvtag_regex')
    def _is_valid_pvtag_regex(self, proposal):
        value = proposal.value
        try:
            for vprefix in self.tag_vprefixes:
                v = self.interpolations.interp(
                    value,
                    pname='<pname>', vprefix=vprefix)
                re.compile(v)
        except Exception as ex:
            proposal.trait.error(None, value, ex)
        return value

    def is_good(self):
        "If format patterns are missing, spurious NPEs will happen when using project."
        return bool(self.tag_vprefixes and
                    self.pvtag_format and
                    self.pvtag_regex)

    tag = Bool(
        config=True,
        help="""
        Enable tagging, per-project.

        Adds a signed tag with name/msg from `tag_name`/`message` (commit implied).

        """)

    message_summary = Unicode(
        "{pname}-{vprefix}{current_version} -> {version}",
        config=True,
        help="""
            The commit & tag message's summary-line part for this project.

            Available interpolations (apart from env-vars prefixed with '$'):
            {vprefix}, {ikeys}
        """)

    def summary_interped(self, is_release=False):
        return self.interp(self.message_summary,
                           vprefix=self.tag_vprefixes[int(is_release)])

    message_body = Unicode(
        config=True,
        help="""
            The commit & tag message-body part for this project.

            Available interpolations (apart from env-vars prefixed with '$'):
            {ikeys}
        """)

    def tag_regex(self, is_release=False) -> Pattern:
        """
        Interpolate and compile as regex.

        :param is_release:
            `False` for version-tags, `True` for release-tags
        """
        vprefix = self.tag_vprefixes[int(is_release)]
        regex = self.interp(self.pvtag_regex,
                            vprefix=vprefix,
                            _escaped_for='regex')
        return re.compile(regex)

    _pvtags_collected = ListTrait(
        Unicode(), allow_none=True, default_value=None,
        help="Populated internally by `populate_pvtags_history()`.")

    @property
    def pvtags_history(self) -> List[str]:
        """
        Return the full *pvtag* history for the project, if any.

        :raise AssertionError:
           If used before :func:`populate_pvtags_history()` applied on this project.
        """
        if self._pvtags_collected is None:
            raise AssertionError("Call first `populate_pvtags_history()` on %s!")
        return self._pvtags_collected

    def version_from_pvtag(self, pvtag: str,
                           is_release: Optional[bool] = None) -> Optional[str]:
        """Extract the version from a *pvtag*."""
        release_flags = [0, 1] if is_release is None else [bool(is_release), ]
        for r in release_flags:
            m = self.tag_regex(r).match(pvtag)
            if m:
                mg = m.groupdict()

                return mg['version']

    def git_describe(self, *git_args: str,
                     include_lightweight=False,
                     is_release=None,
                     **git_flags: str):
        """
        Gets sub-project's version as derived from ``git describe`` on its *pvtag*.

        :param include_lightweight:
            Consider also non-annotated tags when derriving description;
            equivalent to ``git describe --tags`` flag.
        :param is_release:
            a 3-state boolean used as index into :data:`tag_vprefixes`:

            - false: v-tags searched;
            - true: r-tags searched;
            - None: both tags searched.
        :param git_args:
            CLI options passed to ``git describe`` command.
            See :class:`.oscmd.PopenCmd` on how to specify cli options
            using python functions, e.g. ``('*-v*', '*-r*')``
        :param git_flags:
            CLI flags passed to ``git describe`` command.

            - See :class:`.oscmd.PopenCmd` on how to specify cli flags
              using python functions, e.g. ``(all=True)``.
            - See https://git-scm.com/docs/git-describe
        :return:
            the *pvtag* of the current project, or raise
        :raise GitVoidError:
            if sub-project is not *pvtagged*.
        :raise NoGitRepoError:
            if CWD not within a git repo.
        :raise sbp.CalledProcessError:
            for any other error while executing *git*.

        .. Tip::
           There is also the python==2.7 & python<3.6 safe :func:`polyvers.polyversion()``
           for extracting just the version part from a *pvtag*; use this one
           from within project sources.

        .. Tip::
           Same results can be retrieved by this `git` command::

               git describe --tags --match <PROJECT>-v*

           where ``--tags`` is needed to consider also non-annotated tags,
           as ``git tag`` does.
        """
        from .import pvtags

        ## TODO: Project should reuse pvlib as entry-points
        release_flags = [0, 1] if is_release is None else [bool(is_release), ]
        tag_patterns = [self.tag_fnmatch(i) for i in release_flags]

        ## TODO: move to pvtags
        with pvtags.git_project_errors_handled(self.pname):
            out = cmd.git.describe._(
                tags=(include_lightweight) or None,
                *git_args,
                **git_flags)(*('--match=%s' % i for i in tag_patterns))

        version = out

        ## `git describe --all` fetches 'tags/` prefix.
        if 'all' in git_flags:
            version = version.lstrip('tags/')

        if not self.version_from_pvtag(version, is_release):
            raise trt.TraitError(
                "Project-version '%s' fetched by %i patterns (%s) "
                "was unparsable by regex:%s" %
                (version,
                 len(tag_patterns), ', '.join(tag_patterns),
                 ','.join('\n%r' % self.tag_regex(r).pattern
                          for r in release_flags)))

        return version

    def last_commit_tstamp(self):
        """
        Report the timestamp of the last commit of the git repo.

        :return:
            last commit's timestamp in :rfc:`2822` format

        :raise GitVoidError:
            if there arn't any commits yet or CWD not within a git repo.
        :raise sbp.CalledProcessError:
            for any other error while executing *git*.

        .. NOTE::
           Same results can be retrieved by this `git` command::

               git describe --tags --match <PROJECT>-v*

           where ``--tags`` is needed to consider also unannotated tags,
           as ``git tag`` does.
        """
        from .import pvtags

        with pvtags.git_project_errors_handled(self.pname):
            out = cmd.git.log(n=1, format='format:%cD')  # TODO: traitize log-date format

        return out

    def tag_version_commit(self, msg, *,
                           is_release=False, amend=False,
                           sign_tag=None, sign_user=None):
        """
        Make a tag on current commit denoting a version-bump.

        :param is_release:
            `False` for version-tags, `True` for release-tags
        """
        import subprocess as sbp
        from . import pvtags

        tag_name = self._format_vtag(self.version, is_release)
        ## TODO: move all git-cmds to pvtags?
        try:
            out = cmd.git.tag(
                tag_name,
                message=msg,
                force=amend or self.is_forced('tag') or None,
                sign=sign_tag or None,
                local_user=sign_user or None,
            )

            if self.dry_run:
                self.log.warning('PRETEND tag: %s' % out)
        except sbp.CalledProcessError as ex:
            if "already exists" in str(ex.stderr):
                raise pvtags.GitError(
                    "Cannot bump, tag '%s' already exists!"
                    "\n  Add `--force=tag` if you must, or you can --amend." % tag_name)
            raise

    engraves = ListTrait(
        autotrait.AutoInstance(Engrave),
        default_value=[
            {
                'name': 'setup.py',
                ## TODO: add global engrave/project Excludes
                'globs': ['!*egg*', 'setup.py'],
                'grafts': [{
                    'name': 'version-comma',
                    'regex': tw.dedent(r'''
                        (?xm)
                            \bversion
                            (\ *=\ *)
                            .+?(,
                            \ *[\n\r])+
                        '''),
                    'subst': r"version\1'{version}'\2"
                }],
            }, {
                'name': 'py-version',
                'globs': ['!*egg*', '__init__.py', '_version.py'],
                'grafts': [{
                    'name': '__version__',
                    'regex': tw.dedent(r'''
                        (?xm)
                            ^__version__
                            (\ *=\ *)
                            (.+?)$
                        '''),
                    'subst': r"__version__\1'{version}'"
                }, {
                    'name': '__updated__',
                    'regex': tw.dedent(r'''
                        (?xm)
                            ^__updated__
                            (\ *=\ *)
                            (.+?)$
                        '''),
                    'subst': r"__updated__\1'{release_date}'"
                }],
            }, {
                'name': 'readme',
                'globs': ['!*egg*', 'README.rst'],
                'grafts': [{
                    'name': '|version|',
                    'regex': r'\|version\|',
                    'subst': "{version}"
                }, {
                    'name': '|today|',
                    'regex': r'\|today\|',
                    'subst': "{release_date}"
                }],
            },
        ],
        config=True,
        help="""
        """)

    enabled_engraves = SetTrait(
        Unicode(),
        config=True,
        help="""
        Reference by name Engraves that should be active.  If empty, all are active!
        """
    )

    def active_engraves(self):
        actives = self.enabled_engraves
        if not actives:
            return self.engraves

        return [e for e in self.engraves if e.name in actives]

    default_version_bump: str = Unicode(  # type: ignore # noqa: E704 #@IgnorePep8
        '^1',
        config=True,
        help="Which relative version to imply if not given in the cmd-line."
    )

    @trt.validate('default_version_bump')
    def _require_relative_version(self, change):
        if not vermath.is_version_id_relative(change.new):
            raise trt.TraitError(
                "Expected a relative version for '%s.%s', but got '%s'!"
                "\n  Relative versions start either with '+' or '^'." %
                change.owner, change.trait.name, change.new)
