from pspec import describe
from pspec.assertions import assert_raises

with describe('assert_raises'):
    def it_does_not_do_anything_if_correct_exception_is_raised():
        def test():
            with assert_raises(TypeError):
                raise TypeError

        test()

    def it_fails_if_no_exception_is_raised():
        def test():
            with assert_raises(TypeError):
                assert 1

        try:
            test()
        except AssertionError:
            pass # success!
        else:
            raise AssertionError('assert_raises did not raise AssertionError')

    def it_fails_if_incorrect_exception_is_raised():
        def test():
            with assert_raises(TypeError):
                raise IndexError

        try:
            test()
        except Exception:
            pass # success!
        else:
            raise AssertionError('assert_raises did not pass through exception')


