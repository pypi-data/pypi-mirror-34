from . import Unknown, Regex
from . import clan
from . import data
from . import log
from . import thread
from . import pages, dynamiclist
from lxml import etree
import typing
import io

parser = etree.HTMLParser()


class Forum(data.Data):

    cache = {}

    def __init__(self, num: int = 0, *, archive=False):
        """
        Get forum by ID
        """

        super().__init__()

        # Set the ID
        self.id    = num
        self.title = Unknown

        # Prepare fields
        self.archive  = archive
        self.clan     = clan.Clan.cache.get(num, Unknown)
        self.pages    = pages.Pages("threads?id="+str(self.id)+"&page=", self.read_request)
        self.sub      = dynamiclist.DynamicList(self.pages)

    def read_request(self, page, r, t=None):

        return self.read_page(r.text, t, page=page)

    def read_page(self, text, tree=None, page=None) -> typing.Generator[thread.Thread, None, None]:

        # If the text isn't parsed
        if not tree:

            log.receive("Reading messages from " + str(self.id))

            # Parse it
            t = etree.parse(io.StringIO(text), parser)

        # Get root
        root = tree.getroot()

        # Find the title
        n = root.cssselect(".rr")[0]

        # Get the text
        self.title = n.text.replace("\n\t", "")
        self.title = self.title.strip("\r\n")

        # Find all threads
        for el in root.cssselect("div.thread a"):

            # Create thread object
            th = thread.Thread(int(Regex.id.search(el.attrib["href"]).group(1)))

            # Set the title
            th.title = "".join(el.itertext()).strip()

            # Check if is pinned, reliable
            th.pinned = "attached" in el.attrib["class"].split(" ")

            # Check if is closed
            if not th.pinned: th.closed = "grey1" in el.attrib["class"].split(" ")

            yield th

    def load(self, key=None, text=Unknown, *, client=None):

        # If the text hasn't been downloaded
        if text is Unknown:

            ...

    def get_archive(self, archive=True):
        """
        Get archived or unarchived version of self.
        """

        return __class__(self.id, archive=archive)
