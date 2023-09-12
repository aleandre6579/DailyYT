import json
import requests
from tqdm import tqdm


class YTStats:

    def __init__(self, api_key, access_token):
        self.api_key = api_key
        self.access_token = access_token
        self.channel_statistics = None
        self.video_data = None
        self.subscriptions = None
        self.activities = None

    def extract_all(self):
        self.get_channel_statistics()
        self.get_channel_video_data()


    # Get your channel's subscriptions
    def get_my_subscriptions(self):
        print('get channel subscriptions...')
        url = f'https://youtube.googleapis.com/youtube/v3/subscriptions?part=snippet&mine=true&key={self.api_key}&access_token={self.access_token}'
        pbar = tqdm(total=1)
        
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data
        except KeyError:
            print('Could not get channel subscriptions')
            data = {}

        self.subscriptions = data
        pbar.update()
        pbar.close()
        return data
    
    # Get a channel's activities
    def get_channel_activities(self, channelId, maxResult):
        print('get channel activities...')
        url = f'https://www.googleapis.com/youtube/v3/activities?part=snippet,contentDetails&channelId={channelId}&maxResults={maxResult}&key={self.api_key}'
        pbar = tqdm(total=1)
        
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data
        except KeyError:
            print('Could not get channel activities')
            data = {}

        self.activities = data
        pbar.update()
        pbar.close()
        return data 

    # Get a categorie's title
    def get_category_title(self, categoryId):
        print('get category title...')
        url = f'https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&id={categoryId}&key={self.api_key}'
        pbar = tqdm(total=1)
        
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data
        except KeyError:
            print('Could not get category title')
            data = {}

        self.activities = data
        pbar.update()
        pbar.close()
        return data 
    
    # Get a video's info
    def get_video_info(self, videoId):
        print('get video info...')
        url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={videoId}&key={self.api_key}'
        pbar = tqdm(total=1)
        
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data
        except KeyError:
            print('Could not get video info')
            data = {}

        self.activities = data
        pbar.update()
        pbar.close()
        return data 