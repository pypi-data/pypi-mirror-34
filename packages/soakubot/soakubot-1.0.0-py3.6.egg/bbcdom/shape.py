import typing
from . import tag


class AttrDoesntMatch(Exception): pass


class Shape:

    def __init__(self, name: str, value: bool=True, attr: typing.Union[bool, list]=False,
                 rules=lambda attr: True, strip=False):

        self.name  = name.lower()
        self.value = value
        self.attr  = attr
        self.rules = rules
        self.strip = strip

    # noinspection PyShadowingBuiltins
    def tag(self, begin=True, *, attr=""):

        # If it's a begin tag
        if begin:

            # If it accepts value
            if self.value:

                # Set it to a begin tag
                type = tag.Tag.BEGIN

            else:

                # Set it to an empty tag
                type = tag.Tag.EMPTY

        else:

            # Set it to an end tag
            type = tag.Tag.END

        # Create the tag
        t = tag.Tag(self.name, type=type)

        # If attribute matches
        if (not attr or self.rules(attr)) and self.attr == bool(attr) or (isinstance(self.attr, list) and attr in self.attr):

            t.attr = attr

        else: raise AttrDoesntMatch

        return t
