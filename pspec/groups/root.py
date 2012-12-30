import imp
import os
from .base import BaseGroup

class RootGroup(BaseGroup):
    """
    A group that represents a spec module.
    """
    # Name of magic group
    magic_group_name = '_pspec_group'

    def __init__(self, *args, **kwargs):
        super(RootGroup, self).__init__(*args, **kwargs)

        # Spec is the root collecting group
        self.is_collecting = True

    @classmethod
    def from_frame(cls, frame):
        """
        Returns the RootGroup for a given frame, creating a new one if it doesn't 
        exist.
        """
        if cls.magic_group_name not in frame.f_locals:
            filename = frame.f_locals['__file__']
            if filename.endswith('.pyc'):
                filename = filename[:-1]
            spec = RootGroup(filename)
            frame.f_locals[cls.magic_group_name] = spec
            return spec
        return frame.f_locals[cls.magic_group_name]


