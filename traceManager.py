import datetime
seen_recently = dict()

lastTrace = 1

def process(plane):
    global lastTrace
    global  seen_recently
    flight = plane["flight"]
    if flight in seen_recently:
        if seen_recently[flight][1] < datetime.datetime.now()-datetime.timedelta(minutes=5):
            del seen_recently[flight]
        else:
            seen_recently[flight] = (seen_recently[flight][0], datetime.datetime.now())
            return seen_recently[flight][0]

    lastTrace += 1
    seen_recently[flight] =  (lastTrace, datetime.datetime.now())
    return lastTrace