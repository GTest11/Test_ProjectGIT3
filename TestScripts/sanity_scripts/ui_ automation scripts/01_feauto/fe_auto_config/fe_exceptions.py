import logging
class FEStandardError(Exception):
    """
    Base class for all standard Falcon Eye exceptions that do not represent
    interpreter exiting.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class FENavigationError(FEStandardError):
    logging.warning(msg=None)