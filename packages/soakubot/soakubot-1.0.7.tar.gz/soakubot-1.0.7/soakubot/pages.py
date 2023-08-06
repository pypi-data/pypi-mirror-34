from lxml import etree
from io import StringIO
from . import Unknown, PreparedCall, UnknownClient
from . import Regex
from . import data
from . import client as mclient
from . import log


parser = etree.HTMLParser()


class Pages(data.Data):
    """
    Object for iterating through the pages
    """

    cache = {}
    id_type = str

    def __init__(self, url, parse=(lambda p, r, t: r), client=None, protection=mclient.Client.VIEW):

        super().__init__()

        self.url  = url
        self.page = 1
        self.parse = parse
        self.last = Unknown
        self.client = client
        self.protection = protection
        self.all = []

    @classmethod
    def decorator(cls, url, client, protection):

        def ret(func):

            return cls(url, func, client, protection)

        return ret

    def append(self, *args):
        """
        Add all arguments to cache
        """

        self.all.extend(args)

    def __call__(self, page=None, last=None, *, client=None):
        self.page = page or self.page
        self.last = last or self.last
        self.client = client or self.client

        return self

    def __iter__(self):
        self.page = 1

        return self

    def __next__(self, page=None, client=None):

        force = page

        # If argument wasn't given
        if page is None:

            # Get the page
            page = self.page

            # Increment it
            self.page += 1

        # Get client
        c = mclient.get_client(self.__next__, client or self.client, page=page)

        # If it's a prepared call, raise an exception to avoid infinite loops
        if mclient.prepared(c): raise UnknownClient

        # Check if the last page has been crossed
        if not force and isinstance(self.last, int) and page > self.last:

            # Raise exception
            raise StopIteration

        # Log
        log.receive("Reading page", page, "from", self.url)

        # Request
        r = c.get(self.url+str(page), protection=self.protection)

        # Get the parsed HTML
        t = r[1]

        # Load the last page
        self.get_last(t, True)

        # Return it
        return self.parse(page, r[0], t)

    def get_last(self, tree, force=False):

        # If the last page is unknown
        if self.last is Unknown or force:

            # Find the navigation
            arrow = tree.getroot().cssselect('[alt="»"]')

            # Check if navigation is available
            if arrow:

                # Get the link
                last = arrow[0].getparent()

                # Get the URL
                url = last.attrib["href"]

                # Extract the page
                self.last = int(Regex.page.search(url).group(1))

            else:

                # No, it's not. The last page is 1
                self.last = 1

        return self.last

    def get(self, page=None):
        """
        Get data from the page
        """

        # If a slice was given
        if isinstance(page, slice):

            # Get each page
            def gen(enum=False):

                # Set the first page
                start = page.start or 1

                # Load it
                n = self.__next__(start)

                # If enum
                if enum:

                    # Add page counter
                    yield start, n

                else:

                    # Just yield it
                    yield n

                start += 1

                # Set stop given the last page (from previous result)
                stop = page.stop or (self.last+1)

                # Set step
                step = page.step or 1

                # Loop on the pages
                for now in range(start, stop, step):
                    n = self.__next__(now)

                    # If enum
                    if enum:

                        # Add page counter
                        yield now, n

                    else:

                        # Just yield it
                        yield n

            return gen

        # If it's negative
        if page < 0:

            # If the last page hasn't been downloaded
            if self.last is Unknown:

                # Load the first page, forcing the load
                self.get(1)

            # Read from the end
            page = self.last + 1 + page

        # It's an int, return it
        return self.__next__(page)

    def __getitem__(self, item):

        return self.get(item)

    def __len__(self): return self.last

    def prev(self):

        # Move to previous page
        self.page -= 1

        # Get the page
        return self.get()

    @mclient.connection
    def next(self, page=None, client=None):

        return self.__next__(page, client=client)
