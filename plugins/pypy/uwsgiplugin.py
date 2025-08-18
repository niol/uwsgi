NAME = 'pypy'

import os
import subprocess


UWSGI_SRC_DIR = os.getcwd()


LDFLAGS = []
LIBS = []
GCC_LIST = ['pypy_plugin']
BINARY_LIST = [
    ('_uwsgi_pypy_setup', 'pypy_setup.py'),
]
CFLAGS = []
try:
    import __pypy__  # NOQA
    import sys
    CFLAGS.append('-DUWSGI_PYPY_HOME="\\"%s\\""' % sys.prefix)
except ImportError:
    pass


try:
    import cffi
except ImportError:
    cffi = None


def post_build(config):
    if cffi is None:
        print("skipping compile, runtime on-the-fly compile mode only")
        return

    subprocess.call(
        ["pypy3", "pypy_setup.py", "compile"] + config.cflags,
        cwd=os.path.join(UWSGI_SRC_DIR, "plugins", "pypy")
    )
