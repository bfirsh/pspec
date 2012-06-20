from .base import BaseGroup
from .spec import SpecGroup
import os
import re

VALID_MODULE_NAME = re.compile(r'[_a-z]\w*\.py$', re.IGNORECASE)

class FilesystemGroup(BaseGroup):
    """
    A group that contains SpecGroups. It is always a root group.
    """
    def collect(self, start_path):
        """
        Collects tests from a filesystem path. The path can either be a Python file or a 
        directory, under which it will recursively search for tests.
        """

        # Path is a file, turn it into a spec
        if os.path.isfile(start_path):
            self.add_child(SpecGroup.from_path(start_path))
            return

        for root, dirs, files in os.walk(start_path):
            for path in files:
                if not VALID_MODULE_NAME.match(os.path.basename(path)):
                    continue
                # TODO: smarter patterns
                if not path.endswith('_spec.py'):
                    continue
                full_path = os.path.join(root, path)
                self.add_child(SpecGroup.from_path(full_path))



