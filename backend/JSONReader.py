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

def read_act_dates():
    video_dates = []
    with open('acts.json', 'r') as openfile:
        acts_json = json.load(openfile)
    for val in acts_json["items"]:        
        video_dates.append(val['snippet']['publishedAt'])
    return video_dates

def read_act_dates():
    video_dates = []
    with open('acts.json', 'r') as openfile:
        acts_json = json.load(openfile)
    for val in acts_json["items"]:        
        video_dates.append(val['snippet']['publishedAt'])
    return video_dates

def read_video_category_id():
    with open('video_info.json', 'r') as openfile:
        video_json = json.load(openfile)
    return video_json["items"]["snippet"]["categoryId"]

def read_category_title():
    with open('category_info.json', 'r') as openfile:
        category_json = json.load(openfile)
    return category_json["items"]["snippet"]["title"]
