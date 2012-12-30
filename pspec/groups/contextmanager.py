from .base import BaseGroup
from .root import RootGroup
import inspect

class ContextManagerGroup(BaseGroup):
    """
    A group that gathers tests with a context manager.
    """
    def __enter__(self):
        self.is_collecting = True

        frame = inspect.currentframe(1)
        self.spec = RootGroup.from_frame(frame)

        self.parent = self.spec.get_collecting_group()
        self.parent.children.append(self)

        # Collect the locals before with statement so we can figure out what has been
        # defined within it
        self.locals_before = dict(frame.f_locals)

    def __exit__(self, type, value, tb):
        # Exception was raised within the block, raise
        if tb is not None:
            return

        descendant_tests = self.get_descendant_tests()

        self.is_collecting = False
        frame = inspect.currentframe(1)

        new_locals = []

        for name, value in frame.f_locals.items():
            # Assume anything callable is a test
            if not callable(value):
                continue

            # A group further down has got it already
            if value in descendant_tests:
                continue

            # Is this local newly defined or changed within this block?
            if name not in self.locals_before or self.locals_before[name] is not value:
                self.add_test(value)
        

describe = ContextManagerGroup


