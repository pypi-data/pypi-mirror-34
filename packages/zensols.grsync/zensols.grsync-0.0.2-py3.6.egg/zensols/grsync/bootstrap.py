import logging

logger = logging.getLogger('zensols.grsync.bstrap')


class BootstrapGenerator(object):
    SCRIPT = """\
#!/bin/sh

if [ $# -eq 0 ] ; then
    echo "usage: $0 <python_dir> [grsync dir]"
    echo "where: python_dir is the bin directory where python is installed"
    echo "       grsync_dir is the distribution directory copied from the source"
    exit 1
fi
NATIVE_PYTHON_BIN_DIR=$1

if [ $# -eq 2 ]; then
    GRSYNC_INST_DIR=$2
else
    GRSYNC_INST_DIR=`pwd`
fi

PYTHON_DIR=%(python_dir)s
PIP=${PYTHON_DIR}/bin/pip
VIRTUAL_ENV=${NATIVE_PYTHON_BIN_DIR}/virtualenv
PYTHON_PAR=`dirname $PYTHON_DIR`
WHEELS=${GRSYNC_INST_DIR}/%(wheel_dir)s/*.whl

if [ ! -e "${VIRTUAL_ENV}" ] ; then
    echo "virtual environment not installed: 'pip3 install virtualenv'"
    exit 1
fi

echo "bootstrapping python env in ${PYTHON_DIR}, wheels: ${WHEELS}"

rm -rf $PYTHON_PAR

mkdir -p $PYTHON_PAR && \\
    cd $PYTHON_PAR && \\
    ${VIRTUAL_ENV} -p python3 `basename ${PYTHON_DIR}` && \\
    cd - && \\
    ${PIP} install ${WHEELS}

rm ${HOME}/.bash* ${HOME}/.profile*
${PYTHON_DIR}/bin/grsync thaw -d ${GRSYNC_INST_DIR} -t ${HOME}
"""
    SECTION = 'bootstrap'

    def __init__(self, config):
        self.config = config

    def generate(self, path):
        params = self.config.get_options(self.SECTION)
        script = self.SCRIPT % params
        logger.info('creating bootstrap script at: {}'.format(path))
        with open(path, 'w') as f:
            f.write(script)
