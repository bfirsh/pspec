import sys

class Result(object):
    """
    Represents the result of a single test
    """
    def __init__(self, test):
        self.test = test
        self.status = None
        self.exc_type = None
        self.exc_value = None
        self.exc_traceback = None

    def run(self):
        try:
            self.test()
        except KeyboardInterrupt:
            raise
        except:
            self.status = 'fail'
            self.exc_type, self.exc_value, self.exc_traceback = sys.exc_info()
        else:
            self.status = 'pass'

    @property
    def name(self):
        return ' '.join(self.test.__name__.split('_'))




