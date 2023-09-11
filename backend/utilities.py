import json

def writeJSONToFile(filename, dict):
    with open("acts.json", "w") as outfile:
        json.dump(dict, outfile)

