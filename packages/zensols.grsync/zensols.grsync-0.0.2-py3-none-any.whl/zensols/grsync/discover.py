import os
import stat
import socket
import logging
from pathlib import Path
from datetime import datetime
from zensols.grsync import RepoSpec, SymbolicLink

logger = logging.getLogger('zensols.grsync.dc')


class Discoverer(object):
    """
    Discover repositories.
    """
    def __init__(self, config):
        self.config = config

    def _get_repo_paths(self, paths):
        git_paths = []
        for path in paths:
            logger.debug('searching git paths in {}'.format(path.resolve()))
            for root, dirs, files in os.walk(path.resolve()):
                rootpath = Path(root)
                if rootpath.name == '.git':
                    git_paths.append(rootpath.parent)
        return git_paths

    def _relative_to_home(self, path):
        return path.relative_to(Path.home().resolve())

    def _discover_repo_specs(self, paths, links):
        repo_specs = []
        for path in paths:
            logger.debug('found repo at path {}'.format(path))
            repo_spec = RepoSpec(path)
            repo_spec.add_linked(links)
            if len(repo_spec.remotes) == 0:
                logger.warning('repo at {} has no remotes--skipping...'.
                               format(repo_spec))
            else:
                repo_specs.append(repo_spec)
        return repo_specs

    def get_discoverable_objects(self):
        paths = []
        logger.info('finding objects to capture...')
        for fname in self.config.discoverable_objects:
            logger.debug('file pattern {}'.format(fname))
            path = Path(fname)
            bname = path.name
            dname = path.parent.expanduser()
            files = list(dname.glob(bname))
            logger.debug('expanding {} -> {} / {}: {}'.
                         format(path, dname, bname, files))
            paths.extend(files)
        return paths

    def _create_file(self, f):
        mode = f.stat().st_mode
        return {'abs': f,
                'rel': self._relative_to_home(f),
                'modestr': stat.filemode(mode),
                'mode': mode}

    def discover(self):
        dobjs = self.get_discoverable_objects()
        dirs_or_gits = tuple(filter(lambda x: x.is_dir(), dobjs))
        git_paths = self._get_repo_paths(dirs_or_gits)
        links = tuple(map(lambda l: SymbolicLink(l),
                          filter(lambda x: x.is_symlink(), dobjs)))
        files = []
        for f in filter(lambda x: x.is_file() and not x.is_symlink(), dobjs):
            files.append(self._create_file(f))
        repo_specs = self._discover_repo_specs(git_paths, links)
        repo_paths = set(map(lambda x: x.path, repo_specs))
        dirs = []
        for path in filter(lambda x: x not in repo_paths, dirs_or_gits):
            logger.debug('dir {}'.format(path))
            dirs.append({'abs': path, 'rel': self._relative_to_home(path)})
            def gather(par):
                for c in par.iterdir():
                    if c.is_dir():
                        gather(c)
                    elif c.is_file():
                        files.append(self._create_file(c))
            gather(path)
        for r in repo_specs:
            logger.debug('repos spec: {} ({})'.format(r, r.relative_path))
        for link in links:
            logger.debug('link: {}'. format(link))
        for f in files:
            logger.debug('file: {}'.format(str(f)))
        return {'repo_specs': repo_specs,
                'dirs': dirs,
                'files': files}

    def freeze(self):
        disc = self.discover()
        repo_specs = tuple(x.freeze() for x in disc['repo_specs'])
        files = disc['files']
        disc.update({'repo_specs': repo_specs,
                     'files': files,
                     'source': socket.gethostname(),
                     'create_date': datetime.now().isoformat(
                         timespec='minutes')})
        return disc
