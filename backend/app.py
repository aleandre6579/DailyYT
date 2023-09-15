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
VIDEOS_PER_SUB = 2

authorizer = Authorizer(TOKEN_FILE, my_secrets.API_KEY, my_secrets.CLIENT_ID, my_secrets.CLIENT_SECRET)
ACCESS_TOKEN = authorizer.token

yt = YTStats(my_secrets.API_KEY, ACCESS_TOKEN)

## FLASK FUNCTIONS ##

@app.get('/videos')
def send_videos():
    all_videos = get_all_db_videos()
    if all_videos == []:
        return "No videos"
    for video_document in all_videos:
        del video_document['_id']
    return all_videos

@app.get('/refresh')
def refresh_videos():
    new_videos = get_newest_videos()
    return new_videos


def get_subscriptions():
    my_subs = yt.get_my_subscriptions_ids()
    return my_subs

def get_all_db_videos():
    return list(videos.find({}))

def store_video(video):
    videos.insert_one({'videoId': video[0], 'videoTitle': video[1], 'category': video[2], 'thumbnailUrl': video[3]})


def get_newest_videos():
    subs_id = get_subscriptions()
    all_videos_final = []
    for id in subs_id:
        acts = yt.get_channel_activities(id, VIDEOS_PER_SUB)
        writeJSONToFile("acts.json", acts)
        video_ids = read_acts()
        i = 0
        for date in read_act_dates():
            if not videoIsRecent(date, RECENT_IN_DAYS):
                del video_ids[i]
                i -= 1
            i += 1

        # Remove duplicates from youtube API and database
        videos_in_db = get_all_db_videos()
        video_ids = list(set(video_ids))
        for video_id in video_ids:
            for db_video in videos_in_db:
                if video_id == db_video['videoId']:
                    video_ids.remove(video_id)
                    break

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

        new_videos = list(zip(video_ids, video_titles, category_titles, video_thumbnails))
        for new_video in new_videos:
            store_video(new_video)
        all_videos_final += new_videos

    return all_videos_final


if __name__ == "__main__":
    app.run()