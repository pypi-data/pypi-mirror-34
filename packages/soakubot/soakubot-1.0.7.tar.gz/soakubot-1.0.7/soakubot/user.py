import re
from . import Regex, Unknown
from . import data


class User(data.Data):

    cache = {}

    def __init__(self, num):

        super().__init__()

        # Set the ID
        self.id = num

        # Create fields
        self.nick = Unknown
        self.online = Unknown
        self.gender = Unknown

    @classmethod
    def fromlink(cls, link):

        # Find the id
        num = Regex.link.search(link)

        # Create and return the object
        return cls(int(num.group(1)))
