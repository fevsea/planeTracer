import json
import urllib.request

import settings


def getJSON():
    response = urllib.request.urlopen(settings.url)
    data = response.read()
    if response.getcode() != 200:
        return None

    text = data.decode('utf-8')

    try:
        decodedData = json.loads(text)
    except ValueError:
        return None

    return decodedData


def checkValid(item):
    return bool(item["validtrack"])

def checkValidPos(item):
    return bool(item["validposition"])