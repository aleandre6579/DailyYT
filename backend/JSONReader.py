import json
 
# Opening JSON file
with open('subs.json', 'r') as openfile:
    # Reading from json file
    subs_json = json.load(openfile)
 
 
for val in subs_json["items"]:
    print(val['snippet']['title'], val['snippet']['resourceId']['channelId'])