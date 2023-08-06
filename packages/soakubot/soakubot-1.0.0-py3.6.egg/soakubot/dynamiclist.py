from . import UnknownClient
from . import client as mclient
from . import pages


class DynamicList:

    def __init__(self, obj):

        self.pages  = obj

    def __call__(self, page=None, last=None, *, client=None):
        self.pages.page   = page or self.pages.page
        self.pages.last   = last or self.pages.last
        self.pages.client = client or self.pages.client

        return self

    def __iter__(self):

        self.pages.__iter__()
        self.gen = self.generator()

        return self

    def generator(self):

        for x in self.pages:
            yield from x

    def __next__(self, client=None):

        # Read the page
        return self.gen.__next__()
