class Tag:

    BEGIN = 0
    EMPTY = 1
    END   = 2

    def __init__(self, name: str, *, type=BEGIN, attr=""):

        self.name  = name.lower()
        self.type  = type
        self.attr  = attr

    def __repr__(self):

        return str(self)

    def __str__(self):

        if self.type == self.END:

            return "[/"+self.name+"]"

        else:

            return "["+self.name+("="+self.attr if self.attr else "")+"]"
