from . import Unknown
from . import clan
from . import data


class Forum(data.Data):

    cache = {}

    def __init__(self, num: int = 0, *, archive=False):
        """
        Get forum by ID
        """

        super().__init__()

        # Set the ID
        self.id = num

        # Prepare fields
        self.archive  = archive
        self.children = Unknown
        self.clan     = clan.Clan.cache.get(num, Unknown)

    def load(self, key=None, text=Unknown, *, client=None):

        # If the text hasn't been downloaded
        if text is Unknown:

            ...

    def get_archive(self, archive=True):
        """
        Get archived or unarchived version of self.
        """

        return __class__(self.id, archive=archive)
