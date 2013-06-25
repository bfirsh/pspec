"""
Python testing for humans.

Usage: pspec [<path>...]

Options:
  -h --help    show this
"""

from attest.hook import AssertImportHook
from docopt import docopt
import os
import sys
from .collectors import PSpecTests

def main():
    # When run as a console script (i.e. ``pspec``), the CWD isn't
    # ``sys.path[0]``, but it should be.
    cwd = os.getcwd()
    if sys.path[0] not in ('', cwd):
        sys.path.insert(0, cwd)

    arguments = docopt(__doc__)
    paths = arguments['<path>']
    if not paths:
        paths = [name for name in os.listdir('.') 
                 if os.path.isfile('%s/__init__.py' % name)]
    with AssertImportHook():
        tests = PSpecTests(paths)

    tests.run()

if __name__ == '__main__':
    main()

