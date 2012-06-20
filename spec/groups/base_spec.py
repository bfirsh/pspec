import types
from pspec import describe
from pspec.groups.base import BaseGroup
from fixtures import random_spec

with describe('BaseGroup'):
    with describe('get_results'):
        def it_returns_a_generator():
            group = random_spec._pspec.children[0].children[0]
            assert isinstance(group.get_results(), types.GeneratorType)

        def it_returns_a_result_object_for_every_test_within_itself():
            group = random_spec._pspec.children[0].children[0]
            assert len(list(group.get_results())) == 2

        def it_returns_result_objects_for_descendant_tests():
            assert len(list(random_spec._pspec.get_results())) == 5

    with describe('add_child'):
        def it_adds_a_group_to_its_children_and_sets_parent():
            group_a = BaseGroup()
            group_b = BaseGroup()
            group_a.add_child(group_b)
            assert group_a.children == [group_b]
            assert group_b.parent == group_a

    with describe('get_collecting_group'):
        def it_returns_none_by_default():
            assert BaseGroup().get_collecting_group() is None

        def it_returns_own_group_if_it_is_collecting_and_has_no_children():
            group = BaseGroup()
            group.is_collecting = True
            assert group.get_collecting_group() == group

        def it_returns_a_collecting_child_before_itself():
            group = BaseGroup()
            group.add_child(BaseGroup())

            group.is_collecting = True
            group.children[0].is_collecting = True

            assert group.get_collecting_group() == group.children[0]

        def it_returns_rightmost_collecting_child():
            group = BaseGroup()
            group.add_child(BaseGroup())
            group.add_child(BaseGroup())

            group.children[0].is_collecting = True
            group.children[1].is_collecting = True

            assert group.get_collecting_group() == group.children[1]

    with describe('get_descendant_tests'):
        def it_returns_descendant_tests():
            assert len(random_spec._pspec.get_descendant_tests()) == 5

        def it_does_not_return_own_tests():
            group = random_spec._pspec.children[0].children[0]
            assert len(group.get_descendant_tests()) == 0

    with describe('get_tests'):
        def it_returns_descendant_tests():
            print len(random_spec._pspec.get_tests())
            assert len(random_spec._pspec.get_tests()) == 5

        def it_returns_own_tests():
            group = random_spec._pspec.children[0].children[0]
            assert len(group.get_tests()) == 2


