import requests
import json
from time import gmtime, strftime
import time
import ast


# takes file to write to, returns time & contracts appended to file
def addToPastData(betID=7730, filename="pastData.txt"):
    response = requests.get("https://www.predictit.org/api/marketdata/markets/3633")
    data = json.loads(response.content)

    f = open(filename, "a+")
    for b in data["contracts"]:
        if b["id"] == betID:
            f.writelines(str(b) + "\n")
    f.close()

    return strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - " + str(data)


# reads file with filename, returns [contractAtT0, contractAtT1, ...]
def readPastData(filename="pastData.txt"):
    f = open(filename, "r")
    out = []

    for l in f.readlines():
        out.append(ast.literal_eval(l))

    f.close()
    return out


hoursPassed = 0
runtime = 24 * 7
while (hoursPassed < runtime):
    print(addToPastData())
    time.sleep(60^3*1000)
    hoursPassed += 1

print(readPastData())
