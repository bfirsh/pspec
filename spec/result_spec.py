from pspec import describe

from pspec.result import Result

with describe('Result'):
    with describe('run'):
        def it_records_a_passing_test():
            def passing_test():
                assert 1 == 1

            result = Result(passing_test)
            assert result.status is None
            result.run()
            assert result.status == 'pass'

        def it_records_a_failing_test():
            def failing_test():
                assert 1 == 2

            result = Result(failing_test)
            result.run()
            assert result.status == 'fail'
            assert result.exc_type == AssertionError
        
        def it_creates_a_name_from_the_function_name():
            def it_does_something():
                assert True

            result = Result(it_does_something)
            assert result.name == 'it does something'

