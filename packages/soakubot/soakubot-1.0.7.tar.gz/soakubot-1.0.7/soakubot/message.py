import bbcdom
import datetime

from . import log
from . import user
from . import client as mclient
from . import data
from . import thread


class Message:
    """
    Class storing a forum message. Not intended for direct use.
    """

    def __init__(self, num: int, thr: int=0, text: bbcdom.BBCDOM=bbcdom.BBCDOM(), author: int=0, page=None):

        super().__init__()

        # Save the ID
        self.id = num

        # Create fields
        self.thread = thread.Thread(thr)
        self.author = user.User(author)
        self.text   = text
        self.date   = datetime.datetime.now()
        self.page   = page

    @mclient.connection
    def edit(self, text, client=None):

        # Log it
        log.send("Editing message", self.id)

        # Send the request
        client.post("update_message", {
            "message_id":   str(self.id),
            "thread_id":    str(self.thread.id),
            "message_text": str(text),
            "page":         "1"
        })

        # Save the change
        self.text = bbcdom.BBCDOM(text)

        return self

    @staticmethod
    def get_date(string):

        # TODO: Get datetime object from string
        return string
