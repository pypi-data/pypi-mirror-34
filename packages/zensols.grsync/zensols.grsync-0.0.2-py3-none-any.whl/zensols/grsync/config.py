import configparser
from pathlib import Path

from zensols.actioncli import Config


class AppConfig(Config):
    def __init__(self, config_file=None, default_section='default',
                 default_vars=None):
        Config.__init__(self, config_file, default_section, default_vars)

    def _create_config_parser(self):
        inter = configparser.ExtendedInterpolation()
        return configparser.ConfigParser(interpolation=inter)

    @property
    def discoverable_objects(self):
        return map(lambda x: x.strip(),
                   self.get_option_list('objects', expect=True))

    @property
    def dist_dir(self):
        return Path(self.get_option('dist_dir', 'local', expect=True))

    @dist_dir.setter
    def dist_dir(self, dist_dir):
        if self.default_vars is None:
            self.default_vars = {}
        self.default_vars['dist_dir'] = dist_dir

    @property
    def wheel_dir_name(self):
        return self.get_option('wheels_dir', 'local', expect=True)

    @property
    def bootstrap_script_file(self):
        return Path(self.dist_dir, 'bootstrap.sh')
