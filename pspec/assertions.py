from contextlib import contextmanager

@contextmanager
def assert_raises(expected):
    try:
        yield
    except Exception as e:
        exc_type = type(e)
        if not issubclass(exc_type, expected):
            # let unexpected exceptions pass through
            raise
    else:
        try:
            exc_name = expected.__name__
        except AttributeError:
            exc_name = str(expected)
        raise AssertionError("%s not raised" % exc_name)


