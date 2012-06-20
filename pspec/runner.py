# -*- coding: utf-8 -*-
#
from clint.textui import puts, indent, colored
import sys
from .utils import pluralize

class Runner(object):
    """
    Runs tests.
    """
    def __init__(self, group):
        self.group = group
        self.stream = sys.stdout
        self.reset()

    def reset(self):
        self.passes = 0
        self.failures = 0

    def run(self):
        puts()

        self.run_group(self.group)

        if self.failures == 0:
            puts(colored.green('✔ %s test%s passed' % (
                self.passes, 
                pluralize(self.passes),
            )))
        else:
            puts(colored.red('✖ %s of %s test%s failed' % (
                self.failures, 
                self.passes + self.failures,
                pluralize(self.passes + self.failures),
            )))

        puts()

    def run_group(self, group):
        if group.subject:
            puts(group.subject)
            
            with indent(2):
                for result in group.get_results(descendants=False):
                    if result.status == 'pass':
                        puts(colored.green('✓') + ' ' + result.name)
                        self.passes += 1
                    else:
                        puts(colored.red('  ' + result.name))
                        self.failures += 1

                for child in group.children:
                    self.run_group(child)

            puts()

        else:
            for child in group.children:
                self.run_group(child)


def run(group):
    Runner(group).run()


