import logging
from pathlib import Path

logger = logging.getLogger('zensols.grsync.dom')


class PathUtil(Path):
    @classmethod
    def relative_to_home(clz, path):
        return path.relative_to(Path.home().resolve())

    @classmethod
    def expand_home(clz, path):
        return Path.joinpath(Path.home(), path)


class SymbolicLink(object):
    def __init__(self, source):
        self.source = source

    @property
    def target(self):
        return self.source.resolve()

    @property
    def source_relative(self):
        if not hasattr(self, '_src'):
            self._src = PathUtil.relative_to_home(self.source)
        return self._src

    @property
    def target_relative(self):
        if not hasattr(self, '_dst'):
            self._dst = PathUtil.relative_to_home(self.target)
        return self._dst

    def freeze(self):
        return {'source': str(self.source_relative),
                'target': str(self.target_relative)}

    def __str__(self):
        return '{} -> {}'.format(self.source, self.target)

    def __repr__(self):
        return self.__str__()


class RemoteSpec(object):
    def __init__(self, remote, is_master=None, rdef=None):
        self.remote = remote
        with remote.config_reader as cr:
            self.url = cr.get('url')
        self.is_master = is_master

    @property
    def name(self):
        return self.remote.name

    def rename(self, name, url=None):
        remote = self.remote
        remote.rename(name)
        with remote.config_writer as cw:
            if url is not None:
                cw.set('url', url)
            self.repo.git.config('branch.master.pushremote', name)

    def freeze(self):
        return {'name': self.name,
                'url': self.url,
                'is_master': self.is_master}

    def __str__(self):
        return '{}: {}'.format(self.name, self.url)

    def __repr__(self):
        return self.__str__()
