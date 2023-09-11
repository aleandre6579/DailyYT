import json
 
def read_subs():
    channel_ids = []
    with open('subs.json', 'r') as openfile:
        subs_json = json.load(openfile)
    for val in subs_json["items"]:
        #print(val['snippet']['title'], val['snippet']['resourceId']['channelId'])
        channel_ids.append(val['snippet']['resourceId']['channelId'])
    return channel_ids

def read_acts():
    video_ids = []
    with open('acts.json', 'r') as openfile:
        acts_json = json.load(openfile)
    for val in acts_json["items"]:
        #print(val['snippet']['title'], val['contentDetails']['upload']['videoId'])
        
        # Can be either upload or playlistItem
        if 'upload' in val['contentDetails']:
            video_ids.append(val['contentDetails']['upload']['videoId'])
        else:
            video_ids.append(val['contentDetails']['playlistItem']['resourceId']['videoId'])
    return video_ids