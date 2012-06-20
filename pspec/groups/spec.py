import imp
import os
from .base import BaseGroup

class SpecGroup(BaseGroup):
    """
    A group that represents a spec module.
    """

    def __init__(self, *args, **kwargs):
        super(SpecGroup, self).__init__(*args, **kwargs)

        # Spec is the root collecting group
        self.is_collecting = True

    @classmethod
    def from_frame(cls, frame):
        if '_pspec' not in frame.f_locals:
            filename = frame.f_locals['__file__']
            if filename.endswith('.pyc'):
                filename = filename[:-1]
            spec = SpecGroup(filename)
            frame.f_locals['_pspec'] = spec
            return spec
        return frame.f_locals['_pspec']


    @classmethod
    def from_path(cls, path):
        # Guess at module name - is there a better way to do this?
        name = os.path.basename(path).split('.')[0]

        module = imp.load_source(name, path)
        return module._pspec


