
class BaseGroup(object):
    """
    A collection of tests and other groups.
    
    Groups are stored as a tree. They know of their children and parent.
    """

    def __init__(self, subject=None, children=None, parent=None):
        # An identifier for this group
        self.subject = subject

        # This group's subgroups
        self.children = children or []

        # The group this group inherits from
        self.parent = parent

        self.tests = []
        self.is_collecting = False

    def __repr__(self):
        return u'<%s: %s>' % (self.__class__.__name__, self.subject)

    def add_child(self, group):
        """
        Adds group as a child of this group and sets its parent.
        """
        group.parent = self
        self.children.append(group)

    def get_collecting_group(self):
        """
        Returns the right-most group that is currently collecting from this group 
        downwards.
        """
        for group in reversed(self.children):
            result = group.get_collecting_group()
            if result:
                return result
        if self.is_collecting:
            return self

    def get_descendant_tests(self):
        """
        Returns a flat list of tests from this group's descendants, excluding this 
        group's tests.
        """
        tests = []
        for child in self.children:
            tests.extend(child.tests)
            tests.extend(child.get_descendant_tests())
        return tests

    def __iter__(self):
        """
        Returns a flat list of all tests from this group and its descendants.
        """
        return iter(self.tests + self.get_descendant_tests())

    def add_test(self, test):
        """
        Adds a test to this group.
        """
        assert not hasattr(test, '_pspec_group')

        test._pspec_group = self
        self.tests.append(test)


