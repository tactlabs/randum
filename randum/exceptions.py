class BaseRandumException(Exception):
    """The base exception for all Randum exceptions."""


class UniquenessException(BaseRandumException):
    """To avoid infinite loops, after a certain number of attempts,
    the "unique" attribute of the Proxy will throw this exception.
    """


class UnsupportedFeature(BaseRandumException):
    """The requested feature is not available on this system."""
    def __init__(self, msg, name):
        self.name = name
        super().__init__(msg)
