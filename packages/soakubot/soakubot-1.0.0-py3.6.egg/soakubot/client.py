import requests
import time
import typing
import functools
import threading
from lxml import etree
from io import StringIO

from . import PreparedCall
from . import Unknown
from . import log
from . import user
from . import clients
from . import LogInException

# region Miscellaneous

headers = {
    'Accept-Encoding':           'gzip, deflate',
    'Accept-Language':           'en-GB,en;q=0.9,en-US;q=0.8,pl;q=0.7',
    'Cache-Control':             'max-age=0',
    'Connection':                'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/67.0.3396.99 '
                                 'Safari/537.36'
}
parser    = etree.HTMLParser()
use: dict = {}


class Attributes:
    """
    Object used for syntax sugar to calling using the client.
    """

    def __init__(self, *args, client, **kwargs):

        args = list(args)
        self.client = client
        self.args   = args
        self.kwargs = kwargs

    def __gt__(self, other):
        """
        Call a function using the client
        """

        other(*self.args, **self.kwargs, client=self.client)


# endregion

# TODO: Make it compatible with user.User
class Client:

    EDIT = 5
    VIEW = 0.1

    cache = {}

    def __init__(self, nick, pswd, *, url="http://mrush.pl"):

        # Trim trailing slashes
        self.url = url.strip("/")

        # Set URL
        self.url = str(self.url) + "/"

        # Start session
        self.session = requests.session()

        # Set headers
        self.session.headers.update(headers)

        print(self.session.headers)

        # Log message
        log.send("Logging in as", nick)

        # Login
        r = self.session.post(self.url+"login", {
            "name": nick,
            "password": pswd,
        })

        # Parse the result
        tree = etree.parse(StringIO(r.text), parser)

        # Check if header exists
        if not tree.getroot().cssselect("#header"):
            raise LogInException

        # Add to client list
        clients.append(self)

        # Save data
        self.id   = int(self.session.cookies["id"]) or Unknown
        self.nick = nick

        # Set await for requests
        self.last = 0
        self.block_recent = 0
        self.safe = time.time()

    def use(self, thread=threading.current_thread()):
        global use
        use[thread] = self
        return self

    def get(self, url, *, referer=False, protection=VIEW):

        return self.request(url, referer=referer, protection=protection)

    def post(self, url, data=None, *, referer=False, protection=EDIT):

        x = self.request(url, data, "POST", referer=referer, protection=protection)
        x[1]: etree.ElementTree
        return x

    def request(self, url, data=None, method="GET", *, referer=False, protection=VIEW) \
            -> (requests.Response, etree.ElementTree):
        """
        Read data from given URL with rate limit protection.
        Use session.request if you don't care about getting data from the page.
        """

        # Default value for data
        if not data: data = {}

        # Repeat until success
        while True:

            # Check if client isn't safe
            if self.safe > time.time():

                # Safe-sleep

                # Wait
                time.sleep(self.safe - time.time())

            # Set the headers
            h = {**self.session.headers}

            # Set referer
            if referer: h = {**h, "referer": referer}

            try:

                try:

                    # Perform request
                    r = self.session.request(method, self.url + url, headers=h, data=data)

                except SystemError: pass

            except ConnectionResetError:

                # Increase warning awareness
                self.block_recent += 5

                # Set safe time
                self.safe = time.time() + protection + self.block_recent

                # Show notice
                log.blocked("Connection was reset by host, retrying in", self.safe - time.time(), "seconds")

                # Retry
                continue

            # Set the time
            self.last = time.time()

            # Parse the result
            tree = etree.parse(StringIO(r.text), parser)

            # Find the header
            header = tree.getroot().cssselect("#header")

            # Check if the header is present
            if header:

                # Success, got the data.

                # Set safe time
                self.safe = time.time() + protection + self.block_recent

                # Decrease warning awareness
                if self.block_recent > 0: self.block_recent -= 1

                # Return the result and the parsed tree
                return r, tree

            else:

                # Blocked, can't view the data.

                # Set safe time
                self.safe = time.time() + protection + self.block_recent

                # Increase warning awareness
                self.block_recent += 2

                # Show notice in the log.
                log.blocked("Request was blocked, retrying in", self.safe - time.time(), "seconds")

    @property
    def name(self):
        return self.nick

    def __call__(self, *args, **kwargs):
        """
        Generate Attribute object from this client.
        """

        return Attributes(*args, **kwargs, client=self)

    def __rshift__(self, other: typing.Callable):
        """
        Call a function using this client, without any arguments
        """

        # If there are more than 1 client
        if isinstance(other, typing.Callable) and len(clients) > 1:

            # Execute the given function with self
            return other(client=self)

        else:

            # It's alone, the other is likely the result and not a function nor PreparedCall
            return other

    def __str__(self):
        return f"<Client {self.nick}>"


def get_client(func=None, client=None, *args, **kwargs) -> typing.Union[PreparedCall, Client]:

    # If client was found, return it
    if client: return client

    # If there is only one client, use it
    if len(clients) == 1: client = clients[0]

    # Get default client
    thread = threading.current_thread()
    if thread in use: return use[thread]

    # If it wasn't, wait for it to be given
    return PreparedCall(func, *args, **kwargs)


def connection(func: typing.Callable=None):
    """
    Decorator for functions any type of client connections.
    """

    @functools.wraps(func)
    def alt(*args, client: Client=None, **kwargs):
        c = get_client(alt, client, *args, **kwargs)
        if prepared(c): return c

        return func(*args, client=c, **kwargs)

    return alt


def prepared(client):

    return isinstance(client, PreparedCall)
