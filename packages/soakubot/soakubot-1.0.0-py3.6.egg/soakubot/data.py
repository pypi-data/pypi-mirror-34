from . import Unknown


def _alt(func):

    import functools

    @functools.wraps(func)
    def init(self, *p, **k):
        if hasattr(self, "data_initialized"):
            return
        else:
            self.data_initialized = True
            func(self, *p, **k)

    return init


class Data:
    """
    Class representing a data object (eg. clan, message). WARNING: super().__init__ must be called first in all
    subclasses' __init__'s!
    """

    cache = {}
    id_type = int

    def __new__(cls, num: int=0, *args, **kwargs):
        """
        Load object from cache if available
        """

        # if num isn't an int
        if not isinstance(num, cls.id_type):

            # Raise exception
            raise TypeError(
                "Expected num to be {}, got {} instead".format(
                    type(cls.id_type).__name__,
                    type(num).__name__
                )
            )

        # If the object is in cache
        if num in cls.cache:

            # Return it
            return cls.cache[num]

        else:

            # If the class hasn't been modified yet
            if not hasattr(cls, "data_modified"):

                # Add necessary attributes
                cls.data_modified = True

                # Apply it
                cls.__init__ = _alt(cls.__init__)

            # Create new
            obj = super().__new__(cls)

            # Push it to cache
            cls.cache[num] = obj

            # Return it
            return obj

    def load(self, key=None, *, text=Unknown, client=Unknown):
        """
        Download data set including key, None for default. Should return the downloaded key.
        """

        raise AttributeError

    def __getattribute__(self, key: str):

        # Get the value
        value = super().__getattribute__(key)

        # If the value needs to be downloaded
        if value is Unknown:

            try:

                # Download it
                value = self.load(key)

            except AttributeError:

                # Load wasn't found, just return the value
                return value

            # Load the value
            value = value or super().__getattribute__(key)

        # Return it
        return value
