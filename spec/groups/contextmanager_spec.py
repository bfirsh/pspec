from pspec import describe, run
from pspec.groups.contextmanager import ContextManagerGroup
from fixtures import random_spec, single_level_spec, multiple_level_spec

with describe('ContextManagerGroup'):

    def it_creates_a_spec_on_the_module():
        assert hasattr(single_level_spec, '_pspec_group')

    def it_creates_a_group_with_a_subject():
        assert isinstance(single_level_spec._pspec_group.children[0], ContextManagerGroup)
        assert single_level_spec._pspec_group.children[0].subject == 'random'

    def it_creates_tests_from_functions_within_context_manager():
        spec = single_level_spec._pspec_group
        assert len(spec.tests) == 0
        assert len(spec.children[0].tests) == 1
        assert spec.children[0].tests[0].__name__ == 'it_chooses'

    def it_creates_children_with_a_subject():
        parent = multiple_level_spec._pspec_group.children[0]
        assert len(parent.children) == 1
        assert isinstance(parent.children[0], ContextManagerGroup)
        assert parent.children[0].subject == 'choice'

    def it_creates_tests_from_functions_as_a_child():
        parent = multiple_level_spec._pspec_group.children[0]
        assert len(parent.children[0].tests) == 1

    def it_does_not_collect_tests_that_belong_to_child_groups():
        parent = multiple_level_spec._pspec_group.children[0]
        assert len(parent.tests) == 0

    def it_creates_children_in_correct_order():
        group = random_spec._pspec_group.children[0]
        assert group.children[0].subject == 'shuffle'
        assert group.children[1].subject == 'choice'
        assert group.children[2].subject == 'sample'


