from pspec import describe
from pspec.groups.filesystem import FilesystemGroup

with describe('FilesystemGroup'):
    with describe('collect'):
        def it_collects_tests_from_a_single_python_file():
            group = FilesystemGroup()
            group.collect('fixtures/collect/one_spec.py')
            assert len(group.children) == 1
            assert group.children[0].subject == 'fixtures/collect/one_spec.py'
            assert len(group.children[0].children) == 1
            assert len(group.children[0].children[0].tests) == 1

        def it_collects_tests_from_a_directory():
            group = FilesystemGroup()
            group.collect('fixtures/collect/subdir')
            assert len(group.children) == 1
            assert group.children[0].subject == 'fixtures/collect/subdir/two_spec.py'
            assert len(group.children[0].children) == 1
            assert len(group.children[0].children[0].tests) == 1

        def it_recurses_into_directories():
            group = FilesystemGroup()
            group.collect('fixtures/collect')
            assert len(group.children) == 2

        def it_only_collects_python_modules():
            group = FilesystemGroup()
            group.collect('fixtures/not_specs/text_file')
            assert len(group.children) == 0

        def it_only_collects_python_modules_with_the_correct_name():
            group = FilesystemGroup()
            group.collect('fixtures/not_specs/python_module')
            assert len(group.children) == 0

