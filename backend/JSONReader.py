import json
 
## Reading subs
with open('subs.json', 'r') as openfile:
    # Reading from json file
    subs_json = json.load(openfile)
 
 
for val in subs_json["items"]:
    print(val['snippet']['title'], val['snippet']['resourceId']['channelId'])

## Reading acts
with open('acts.json', 'r') as openfile:
    # Reading from json file
    acts_json = json.load(openfile)
 
print('---')

for val in acts_json["items"]:
    print(val['snippet']['title'], val['contentDetails']['upload']['videoId'])