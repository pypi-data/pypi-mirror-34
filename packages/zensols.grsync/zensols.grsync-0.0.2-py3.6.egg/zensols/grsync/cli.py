import os
from zensols.actioncli import OneConfPerActionOptionsCli
from zensols.grsync import AppConfig
from zensols.grsync import DistManager

VERSION = '0.1'


# recommended app command line
class ConfAppCommandLine(OneConfPerActionOptionsCli):
    def __init__(self):
        dist_dir_op = ['-d', '--distdir', False,
                       {'dest': 'dist_dir', 'metavar': 'DIRECTORY',
                        'help': 'the location of build out distribution'}]
        target_dir_op = ['-t', '--targetdir', False,
                         {'dest': 'target_dir', 'metavar': 'DIRECTORY',
                          'help': 'the location of build out target dir'}]
        cnf = {'executors':
               [{'name': 'discover',
                 'executor': lambda params: DistManager(**params),
                 'actions': [{'name': 'freeze',
                              'doc': 'create a distribution',
                              'opts': [dist_dir_op]},
                             {'name': 'thaw',
                              'doc': 'build out a distribution',
                              'opts': [dist_dir_op, target_dir_op]}]}],
               'config_option': {'name': 'config',
                                 'opt': ['-c', '--config', False,
                                         {'dest': 'config', 'metavar': 'FILE',
                                          'help': 'configuration file'}]},
               'whine': 1}
        super(ConfAppCommandLine, self).__init__(cnf, version=VERSION)

    def _create_config(self, config_file, default_vars):
        defs = {}
        defs.update(default_vars)
        defs.update(os.environ)
        return AppConfig(config_file=config_file, default_vars=defs)


def main():
    cl = ConfAppCommandLine()
    cl.invoke()
