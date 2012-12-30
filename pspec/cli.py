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

