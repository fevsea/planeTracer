import time

import adsbReceiver
import dbUtils
import settings
import traceManager


def process(decodedData):
    for plane in decodedData:
        if not adsbReceiver.checkValid(plane):
            continue
        trace = "NULL"
        if adsbReceiver.checkValidPos(plane):
            trace = str(traceManager.process(plane))
        dbUtils.insert(plane, trace)


if __name__ == "__main__":
    firstIter = True

    while True:
        decodedData = None
        while decodedData == None:
            decodedData = adsbReceiver.getJSON()

        if firstIter:
            dbUtils.initDB(decodedData)
            firstIter = False

        process(decodedData)
        time.sleep(settings.poolingInterval)
