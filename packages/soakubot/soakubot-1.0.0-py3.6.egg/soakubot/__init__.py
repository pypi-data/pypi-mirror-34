import re


clients = []


class Regex:

    page = re.compile(r"[&?]page=(\d+)")
    id   = re.compile(r"[&?]id=(\d+)")
    link = re.compile(r"[&?]player_id=(\d+)")
    user = re.compile(r'<a href="view_profile\?player_id=(\d+)" class="tdn lwhite">([^<]*)</a>')
    date = re.compile(r'<span class="grey1 small">([^<]+)</span>')
    msg       = re.compile(r'<span id="msg(\d+)"></span>'
                           r'(.*?)'
                           r'</span> (?:<br/><span class="grey1 small">([^<]*)</span>| (?:<br ?/?>|[\r\n]{1,2}\t))',
                           re.DOTALL)
    msg_begin = re.compile(r'<span class="l(blue|yell)[^"]+">(.*)', re.DOTALL)
    msg_end   = re.compile(r'</span> <br/><span class="grey1 small">'
                           r'|</span> {2}<br /><span class="grey1 small">'
                           r'\[ <a class="grey1 small" href="/message_delete[^"]*">x</a> '
                           r'\| <a class="grey1 small" href="/message_edit[^"]*">\w+</a> ]</span>\n'
                           r'\t</div><div class="hr_arr mlr10 mb5"><div class="alf">'
                           r'<div class="art"><div class="acn"></div></div></div></div>.*|</span> {2}\n'
                           r'\t</div><div class="hr_arr mlr10 mb5"><div class="alf">'
                           r'<div class="art"><div class="acn"></div></div></div></div>.*', re.DOTALL)
    icon = re.compile(r'<img src="http://144.76.127.94/view/image/icons/hero_(off|on)_([01]).png" class="icon" ?/?>')


class PreparedCall:

    def __init__(self, *args, **kwargs):

        args = list(args)

        self.func = args.pop(0)
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        return self.func(*self.args, *args, **{**self.kwargs, **kwargs})


class UnknownType:
    """Empty object to place in fields with data that hasn't been downloaded yet and needs to."""

    def __bool__(self):
        return False

    def __repr__(self):
        return "Unknown"


Unknown = UnknownType()


class UnknownClient(Exception): pass


class LogInException(Exception): pass


class NoPermissionException(Exception): pass


# THIS MUST BE HERE (circular reference and stuff), STFU PYCHARM
if True:
    from . import log
    from .client import Client
    from .user import User
    from .clan import Clan
    from .data import Data
    from .forum import Forum
    from .thread import Thread
    from .message import Message
    from .dynamiclist import DynamicList
    from .pages import Pages
