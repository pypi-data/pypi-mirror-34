import typing
import re
import html as mhtml
from . import tag
from .shape import Shape


class ContinueParsing(Exception): pass


class Regex:

    begin = re.compile(r"\[(\w+)(?:=([^]\n]+))?\]")
    end   = re.compile(r"\[/(\w+)\]")
    br    = re.compile(r"\r\n|\n|\r")
    color = re.compile(r"^[\w#]+$")


class HTMLRegex:

    nl    = re.compile(r'<br */?>(\r\n|\r|\n)')
    br    = re.compile(r'<br */?>')
    hr    = re.compile(r'<div class="hr_g mb2">(?:<div/?>){2}(?:</div>){0,3}')
    # 0,3 so it correctly parses badly formatted code
    color = re.compile(r'<span style="color: *([#\w]+);">(.*?)</span>')
    font  = re.compile(r'<span class="(large|small)">(.*?)</span>')
    align = re.compile(r'<div class="(center|right)">(.*?)</div>')
    list  = re.compile(r'<(ul|li|[biu])>(.*?)</\1>')
    link  = re.compile(r'<a href="/([^"]+)">(.*?)</a>')
    image = re.compile(r'<img class="icon" height="([^"]+)" src="http://144.76.125.123/([^"]+)"(?: /)?/?>')
    emote = re.compile(r'<img class="smile" src="http://144.76.127.94/view/image/smiles/(\d+).gif" />')


class BBCDOM(list):

    tags = {
        "b":      Shape("b"),
        "i":      Shape("i"),
        "u":      Shape("u"),
        "center": Shape("center"),
        "right":  Shape("right"),
        "ul":     Shape("ul"),
        "li":     Shape("li"),
        "color":  Shape("color", attr=True, rules=lambda a: Regex.color.match(a)),
        "img":    Shape("img", attr=True, strip=True),
        "url":    Shape("url", attr=True),
        "font":   Shape("font", attr=["small", "large"]),
        "br":     Shape("br", value=False),
        "hr":     Shape("hr", value=False),
    }

    def __init__(self, obj: typing.Union[str, tag.Tag]="", plain=False):
        """
        Create BBCDOM object from text. No BBCode errors will be corrected to keep original byte count.
        :param obj: BBCode formatted text
        :param plain: Should the document be read as plain text (without formatting)
        """

        super().__init__()

        if plain:

            super().append(obj)

        else:

            super().extend(self.parse(obj))

    def append(self, obj: typing.Union[str, tag.Tag], plain=False):

        if plain:

            super().append(obj)

        else:

            super().extend(self.parse(obj))

    def strip(self, contents=False):
        """
        Remove every tag from the DOM.
        :return:
        """
        o = 0
        force = 0
        res = []

        for key, x in enumerate(self):

            if isinstance(x, tag.Tag):

                if x.type == x.BEGIN:

                    o += 1

                    try:

                        if force or self.tags[x.name.lower()].strip:

                            force += 1

                    except KeyError:

                        pass

                elif x.type == x.END:

                    o -= 1
                    if force: force -= 1

                else:

                    res += "\n"

            else:

                if not (force or contents and o): res.append(x)

        return "".join(res)

    @classmethod
    def parse(cls, obj):

        # If it's a tag, return it
        if isinstance(obj, tag.Tag):
            return [obj]

        # If it's nothing listed, try to convert it to a string
        obj = str(obj)

        # Begin parsing
        ret       = []
        open_tags = []
        append    = []
        idx       = 0

        def close_open():

            # Close open elements
            for i, t in reversed(list(enumerate(ret))):

                # If open_tags is empty, stop
                if not open_tags: break

                # Continue if it's not a tag
                if not isinstance(t, tag.Tag): continue

                # Continue if the tag isn't open
                if t.name not in open_tags: continue

                # Continue if the tag is not of begin type
                if t.type != t.BEGIN: continue

                # Stringify the tag
                ret[i] = str(t)

                # Remove it from open tags
                open_tags.remove(t.name)

        # Start parse loop
        while idx < len(obj):

            try:

                # Check start of a tag is encountered
                match = Regex.begin.match(obj[idx:])

                # If it is, check it
                for zero in range(match is not None):

                    # Check if it matches a shape
                    if match.group(1).lower() not in cls.tags: break

                    # Get the shape
                    shp = cls.tags[match.group(1).lower()]

                    # Fail if the tag is already opened
                    if match.group(1) in open_tags: break

                    try:

                        # Get the tag
                        t = shp.tag(attr=match.group(2))

                    # If attributes don't match
                    except shape.AttrDoesntMatch:

                        # Fail the match
                        break

                    # If it's not empty
                    if t.type == t.BEGIN:

                        # Append it to opened tag list
                        open_tags.append(t.name)

                    # Append it to result
                    ret.append(t)

                    # Skip it
                    idx += len(match.group(0))

                    # Continue parsing
                    raise ContinueParsing

                # Check if end of a tag is encountered
                match = Regex.end.match(obj[idx:])

                # If it is, check it
                for zero in range(match is not None):

                    # Fail if it's not opened
                    if match.group(1) not in open_tags: break

                    # If the opening tag is last in the DOM
                    if isinstance(ret[-1], tag.Tag) and ret[-1].name == match.group(1):

                        # Stringify it
                        ret[-1] = str(ret[-1])

                        # Parse this as string instead
                        break

                    # Close it
                    ret.append(tag.Tag(match.group(1), type=tag.Tag.END))

                    # Remove it from opened list
                    open_tags.remove(match.group(1))

                    # Skip it
                    idx += len(match.group(0))

                    # Continue parsing
                    raise ContinueParsing

                # Match line breaks
                match = Regex.br.match(obj[idx:])

                # If one was encountered
                for zero in range(match is not None):

                    # Append it
                    if ret and isinstance(ret[-1], str):

                        ret[-1] += obj[idx]

                    else:

                        # Append the str
                        ret.append(obj[idx])

                    # Skip it
                    idx += len(match.group(0))

                    # If no elements are open, continue parsing
                    if not open_tags: raise ContinueParsing

                    # Close open elements
                    close_open()

                    # Continue parsing
                    raise ContinueParsing

                # Not matched by anything else.
                # If the last item is a str, append to it
                if ret and isinstance(ret[-1], str):

                    ret[-1] += obj[idx]

                else:

                    # Append the str
                    ret.append(obj[idx])

                # Skip it
                idx += 1

            # Continue parsing
            except ContinueParsing: pass

        # Close open elements
        close_open()

        # Return the result
        return ret

    @classmethod
    def fromhtml(cls, html: str):
        """
        Create BBCDOM object from HTML.

        WARNING: Do not use already parsed HTML for the argument, as some data might be lost.
        WARNING: Variables (like %%NAME%%) will be lost with this conversion.
        """

        # Parse line breaks
        html = HTMLRegex.nl.sub('\n', html)

        # Parse [br]
        html = HTMLRegex.br.sub('[br]', html)

        # Parse [hr]
        html = HTMLRegex.hr.sub("[hr]", html)

        # Parse [color]
        html = HTMLRegex.color.sub("[color=\\1]\\2[/color]", html)

        # Parse [font]
        html = HTMLRegex.font.sub("[font=\\1]\\2[/font]", html)

        # Parse [center] & [right]
        html = html.replace('"cntr"', '"center"')
        html = html.replace('"rgt"', '"right"')

        # ^ until no changes need to be done
        pre = ""
        while html != pre:
            pre = html
            html = HTMLRegex.align.sub("[\\1]\\2[/\\1]", html)

        # Parse [ul], [li] & inline formatting until no changes need to be done
        pre = ""
        while html != pre:
            pre = html
            html = HTMLRegex.list.sub("[\\1]\\2[/\\1]", html)

        # Parse images
        html = HTMLRegex.image.sub("[img=\\1]\\2[/img]", html)

        # Parse emotes
        html = HTMLRegex.emote.sub("[img=x]emote_code/\\1[/img]", html)

        # Parse links
        html = HTMLRegex.link.sub("[url=\\1]\\2[/url]", html)

        # Unescape HTML
        html = mhtml.unescape(html)

        return cls(html)

    def __str__(self):

        ret = ""

        # For each child
        for ch in self:

            # Stringify it
            ret += str(ch)

        # Return the result
        return ret