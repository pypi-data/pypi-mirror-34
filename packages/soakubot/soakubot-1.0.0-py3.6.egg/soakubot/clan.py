import io
from lxml import etree
from . import Unknown, UnknownClient, PreparedCall
from . import Regex
from . import client as mclient
from . import data
from . import forum
from . import log


parser = etree.HTMLParser()


class Clan(data.Data):

    cache = {}

    def __init__(self, num: int):
        """
        Get clan by ID
        """

        super().__init__()

        # Get clan by ID
        self.id = num

        # Create fields
        self.name     = Unknown
        self.crest    = Unknown
        self.about    = Unknown
        self.created  = Unknown
        self.level    = Unknown
        self.builds   = Unknown
        self.xp       = Unknown
        self.members  = Unknown
        self.history  = Unknown

        # Get forum if it's in cache
        self.forum    = forum.Forum.cache.get(self.id, Unknown)

    def __eq__(self, other):

        # If the other object is a clan
        if isinstance(other, Clan):

            # Compare IDs
            return self.id == other.id

        else:

            # It's not even a clan
            return False

    @mclient.connection
    def load(self, key=None, text=Unknown, *, client=None):

        tree: etree._ElementTree

        # If the html needs to be downloaded
        if text is Unknown:

            # Send message to log
            log.receive("Reading data about clan", self.id)

            # Read the HTML
            text = client.get(f"clan?id={self.id}")[1]

        # If html is a string
        if isinstance(text, str):

            # Parse it
            tree = etree.parse(io.StringIO(text), parser)

        # If html is already parsed
        elif isinstance(text, etree.ElementTree()):

            # Just get_client the tree
            tree = text

        # Get the root
        root = tree.getroot()

        # Get the name
        self.name = (

                # Select name next to the crest
                root.cssselect(".bold.large.mb.ml5")

                # Select name without crest
                or root.cssselect(".rl .rr")

            )[0].text

        # Read other attributes
        ...

    @classmethod
    @mclient.connection
    def byname(cls, name, client: mclient.Client=None):
        """
        Get clan by name
        """

        # Send a message in log
        log.receive("Searching for clans named", name)

        # Perform a search
        r, tree = client.post("find_clan", {
            "name": name
        })

        # Get the ID
        tid = Regex.id.search(r.url).group(1)

        # Create the object
        obj = cls(int(tid))

        # Set known properties
        obj.name = name

        # Parse the data
        obj.load(text=r.text)

        # Return the object
        return obj

    def __str__(self):
        return f"<Category {self.id}>"
