from datetime import datetime


debug = True


def logger(connection):

    def msg(*args):
        if debug: print("[" + str(datetime.now()) + "] " + connection + " " + " ".join([str(x) for x in args]))

    return msg


receive = logger("← ")
send    = logger(" →")
both    = logger("←→")
blocked = logger("|←")
