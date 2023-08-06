import os
import logging
import json
import zipfile
import shutil
from pathlib import Path
from zensols.grsync import Discoverer, RepoSpec, BootstrapGenerator

logger = logging.getLogger('zensols.grsync.dist')


class DistManager(object):
    WHEEL_DEPENDENCY = 'zensols.grsync'

    def __init__(self, config=None, dist_dir=None,
                 target_dir=None, only_repo_names=None):
        self.config = config
        # config will be missing on thaw
        if config is None:
            if dist_dir is None:
                raise ValueError('missing dist file option')
            self.dist_dir = Path(dist_dir)
        else:
            if dist_dir is not None:
                self.config.dist_dir = dist_dir
            self.dist_dir = self.config.dist_dir
        if target_dir is not None:
            self.target_dir = Path(target_dir)
        else:
            self.target_dir = None
        self.only_repo_names = only_repo_names
        self.file_install_path = 'to_install'
        self.defs_file = 'dist.json'
        self.dir_create_mode = 0o755
        self.exec_file_create_mode = 0o755

    @property
    def dist_file(self):
        return Path(self.dist_dir, 'dist.zip')

    def _create_wheels(self):
        wheel_dir_name = self.config.wheel_dir_name
        wheel_dir = Path(self.dist_dir, wheel_dir_name)
        logger.info('creating wheels in {}'.format(wheel_dir))
        if not wheel_dir.exists():
            wheel_dir.mkdir(
                self.dir_create_mode, parents=True, exist_ok=True)
        from pip._internal import main
        dep = Path(self.WHEEL_DEPENDENCY).expanduser().resolve()
        pip_cmd = 'wheel --wheel-dir={} {}'.format(wheel_dir, dep)
        logger.debug('pip cmd: {}'.format(pip_cmd))
        main(pip_cmd.split())

    def _freeze_dist(self):
        dist_file = self.dist_file
        if not self.dist_dir.exists():
            self.dist_dir.mkdir(
                self.dir_create_mode, parents=True, exist_ok=True)
        logger.info('freezing distribution in {}'.format(dist_file))
        disc = Discoverer(self.config)
        data = disc.freeze()
        with zipfile.ZipFile(dist_file, mode='w') as zf:
            for finfo in data['files']:
                fabs = finfo['abs']
                frel = str(Path(self.file_install_path, finfo['rel']))
                logger.debug('adding file: {}'.format(fabs))
                zf.write(fabs, arcname=frel)
                del finfo['abs']
                finfo['rel'] = frel
            if False:
                for dname in data['dirs']:
                    logger.info('adding directory: {}'.format(dname))
                    frel = str(Path(self.file_install_path, dname['rel']))
                    zf.write(dname['abs'], arcname=frel)
            del data['dirs']
            logger.info('writing distribution defs to {}'.
                        format(self.defs_file))
            zf.writestr(self.defs_file, json.dumps(data, indent=2))

    def freeze(self):
        self._freeze_dist()
        script_file = self.config.bootstrap_script_file
        bg = BootstrapGenerator(self.config)
        bg.generate(script_file)
        script_file.chmod(self.exec_file_create_mode)
        # put the wheels last since pip clobers/reconfigures logging
        self._create_wheels()

    def _target_relative(self, path):
        return Path.joinpath(self.target_dir, path)

    def _thaw_remote_specs(self, rdef):
        repo_path = self._target_relative(rdef['path'])
        parent = repo_path.parent
        if not parent.exists():
            logger.info('creating parent directory: {}'.format(parent))
            parent.mkdir(self.dir_create_mode, parents=True, exist_ok=True)
        repo_spec = RepoSpec.thaw(rdef, self.target_dir, repo_path)
        return repo_spec

    def _thaw_repos(self, struct):
        rdefs = {}
        for rdef in struct['repo_specs']:
            name = rdef['name']
            if self.only_repo_names is None or name in self.only_repo_names:
                rdefs[name] = rdef
        for rdef in rdefs.values():
            self._thaw_remote_specs(rdef)

    def _thaw_files(self, struct, zf):
        files = struct['files']
        for finfo in files:
            mode = finfo['mode']
            rel = Path(finfo['rel'])
            path = self._target_relative(Path(os.path.join(*rel.parts[1:])))
            parent = path.parent
            if not parent.exists():
                logger.info('creating parent directory: {}'.format(parent))
                parent.mkdir(mode=self.dir_create_mode, parents=True)
            logger.debug('thawing file: {}'.format(path))
            if path.exists():
                logger.warning('refusing to overrite file {}--skipping'.
                               format(path))
            else:
                with zf.open(str(rel)) as fin:
                    with open(str(path), 'wb') as fout:
                        shutil.copyfileobj(fin, fout)
                logger.debug('setting mode of {} to {} ({})'.
                             format(path, mode, finfo['modestr']))
                path.chmod(mode)

    def thaw(self):
        dist_file = self.dist_file
        logger.info('expanding distribution in {}'.format(dist_file))
        with zipfile.ZipFile(str(dist_file.resolve())) as zf:
            with zf.open(self.defs_file) as f:
                jstr = f.read().decode('utf-8')
                struct = json.loads(jstr)
            self._thaw_files(struct, zf)
            self._thaw_repos(struct)
