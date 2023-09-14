from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient
from pyyoutube import Api
from pyyoutube import Client
from traceback import print_exc
from youtube_stats import YTStats
from authorizer import Authorizer
from utilities import *
from JSONReader import *
from datetime import date
import my_secrets
import json

app = Flask(__name__)
CORS(app)

client = MongoClient('localhost', 27017)
db = client.flask_db
videos = db.videos

# Constants
TOKEN_FILE = "token.json"
RECENT_IN_DAYS = 2

authorizer = Authorizer(TOKEN_FILE, my_secrets.API_KEY, my_secrets.CLIENT_ID, my_secrets.CLIENT_SECRET)
ACCESS_TOKEN = authorizer.token

yt = YTStats(my_secrets.API_KEY, ACCESS_TOKEN)

## FLASK FUNCTIONS ##

#myquery = { "videoId": "videoUrl" }
#videos.delete_one(myquery)

@app.get('/videos')
def send_videos():
    all_videos = get_all_db_videos()
    if all_videos == []:
        return "No videos"
    for video_document in all_videos:
        del video_document['_id']
    print(all_videos)
    return all_videos

@app.get('/refresh')
def refresh_videos():
    new_videos = get_newest_videos()
    for new_video in new_videos:
        store_video(new_video)
    return new_videos

def get_all_db_videos():
    return list(videos.find({}))

def store_video(video):
    videos.insert_one({'videoId': video[0], 'videoTitle': video[1], 'category': video[2], 'thumbnailUrl': video[3]})


def get_newest_videos():
    subs_id = read_subs()
    all_videos_final = []
    for id in subs_id:
        acts = yt.get_channel_activities(id, 3)
        writeJSONToFile("acts.json", acts)
        video_ids = read_acts()
        i = 0
        for date in read_act_dates():
            if not videoIsRecent(date, RECENT_IN_DAYS):
                del video_ids[i]
                i -= 1
            i += 1

        category_titles = []
        video_titles = []
        video_thumbnails = []
        for video_id in video_ids:
            video_info = yt.get_video_info(video_id)["items"][0]["snippet"]
            category_id = video_info["categoryId"]
            category_title = yt.get_category_title(category_id)["items"][0]["snippet"]["title"]
            video_title = video_info["title"]
            video_thumbnail = video_info["thumbnails"]["default"]["url"]

            category_titles.append(category_title)
            video_titles.append(video_title)
            video_thumbnails.append(video_thumbnail)

        all_videos_final += list(zip(video_ids, video_titles, category_titles, video_thumbnails))
    return all_videos_final


if __name__ == "__main__":
    app.run()