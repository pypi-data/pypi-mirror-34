import bbcdom
import typing
import io
from lxml import etree
from . import Unknown, Regex
from . import log
from . import data
from . import pages
from . import dynamiclist
from . import user
from . import message
from . import client as mclient


parser = etree.HTMLParser()


class Thread(data.Data):

    cache = {}

    def __init__(self, num):

        super().__init__()

        # Save the ID
        self.id = num

        # Create fields
        self.title = Unknown
        self.msgs = Unknown
        self.pinned = Unknown
        self.closed = Unknown
        self.deleted = Unknown

        # Anti-anti-spam protection
        self.space = {}

        # Pages
        self.pages = pages.Pages("thread?id="+str(self.id)+"&page=", self.read_request)
        self.msgs = dynamiclist.DynamicList(self.pages)

    def read_request(self, page, r, t=None):

        return self.read_page(r.text, t, page=page)

    def read_page(self, text, tree=None, page=None) -> typing.Generator[message.Message, None, None]:

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

        # Check if the thread is closed
        try:

            # Get link to closer's profile
            link = root.cssselect(".player_name")[0]

            # Find out who closed the thread
            self.closed = user.User.fromlink(link.attrib["href"])

            # Set the nick
            self.closed.nick = link.text

        except IndexError:

            # It's not
            self.closed = False

        # Check for presence of unpin button
        self.pinned = bool(len(root.cssselect('.mbtn[href^="/detach_thread"]')))

        # If the thread doesn't seem to be pinned
        if not self.pinned:

            # Check if pin button is present to make sure mod privileges are available
            self.pinned = False if bool(len(root.cssselect('.mbtn[href^="/attach_thread"]'))) else Unknown

        # Get all messages
        for match in Regex.msg.finditer(text):

            # Create the message object
            msg = message.Message(int(match.group(1)), self.id, page=page)

            # Get remaining content
            text = match.group(2)

            # Find author
            m = Regex.user.search(text)

            # Create author object
            msg.author = user.User(int(m.group(1)))

            # Get author's nick
            msg.author.nick = m.group(2)

            # Get date
            m = Regex.date.search(text)
            msg.date = msg.get_date(m.group(1))

            # Get the message text
            m = Regex.msg_begin.search(text)
            msg.text = bbcdom.BBCDOM.fromhtml(m.group(2))

            # Yield the message
            yield msg

    @classmethod
    @mclient.connection
    def new(cls, forum, title, text, *, client):

        # Log
        log.send("Creating thread", title)

        # Create the thread
        r = client.post("create_thread", {
            "thread_name": str(title),
            "thread_text": str(text),
            "forum_id":    str(forum.id if hasattr(forum, "id") else forum)
        })

        # Create the object
        t = Thread(int(Regex.id.search(r[0].url).group(1)))

        # Set the object's data
        t.title = title
        t.text = bbcdom.BBCDOM(text)

        # Return it
        return t

    @mclient.connection
    def close(self, client):
        log.send("Closing thread", self.id)
        client.get("close_thread?id="+str(self.id))
        self.closed = client
        return self

    @mclient.connection
    def open(self, client):
        log.send("Opening thread", self.id)
        client.get("open_thread?id="+str(self.id))
        self.closed = False
        return self

    @mclient.connection
    def pin(self, client):
        log.send("Pinning thread", self.id)
        client.get("attach_thread?id="+str(self.id))
        self.pinned = True
        return self

    @mclient.connection
    def unpin(self, client):
        log.send("Unpinning thread", self.id)
        client.get("detach_thread?id="+str(self.id))
        return self

    @mclient.connection
    def reply(self, text, target=0, *, client=None):

        log.send("Sending message to thread "+str(self.id))

        # Check if space is needed
        space = " " if self.space.get(client.id, False) else ""

        r = client.post("thread_message", {
            "message_text": space + str(text),
            "answer_id":    str(target),
            "thread_id":    str(self.id)
        })

        # Update space info
        self.space[client.id] = not space

        return list(self.read_page(r[0].text, r[1]))

    def __repr__(self):
        return "<Thread "+str(self.id)+" at "+hex(id(self)).upper()+">"
