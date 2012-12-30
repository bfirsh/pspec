from attest.collectors import Tests
from attest.utils import import_dotted_name, deep_get_members
from .groups.root import RootGroup
import inspect

class PSpecTests(Tests):
    # HACK: Copied from Attest, just to change `istests`
    def register(self, tests):
        if inspect.isclass(tests):
                self._tests.extend(tests())
                return tests
        elif isinstance(tests, basestring):
            def istests(obj):
                return isinstance(obj, (Tests, RootGroup))
            obj = import_dotted_name(tests)
            if inspect.ismodule(obj):
                for tests in deep_get_members(tests, istests, private=True):
                    self.register(tests)
                return
            tests = obj
        for test in tests:
            if not test in self._tests:
                self._tests.append(test)


def run():
    frame = inspect.currentframe(1)
    group = RootGroup.from_frame(frame)
    PSpecTests([group]).run()

