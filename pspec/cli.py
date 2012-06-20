"""
Python testing for humans.

Usage: pspec [<path>...]

Options:
  -h --help    show this
"""

from docopt import docopt
import sys
from .groups.filesystem import FilesystemGroup
from .runner import Runner

def main():
    arguments = docopt(__doc__)
    group = FilesystemGroup()
    if len(arguments['<path>']):
        for arg in arguments['<path>']:
            group.collect(arg)
    else:
        group.collect('.')

    runner = Runner(group)
    runner.run()

    if runner.failures > 0:
        sys.exit(1)
        

