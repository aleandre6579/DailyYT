import json
import requests
from tqdm import tqdm


class YTStats:

    def __init__(self, api_key, access_token):
        self.api_key = api_key
        self.access_token = access_token
        self.channel_statistics = None
        self.video_data = None
        self.subscriptions_ids = None
        self.activities = None

    def get_request_data(self, url):
        pbar = tqdm(total=1)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data
        except KeyError:
            print('Could not get channel activities')
            data = {}
        pbar.update()
        pbar.close()
        return data

    # Get your channel's subscriptions
    def get_my_subscriptions_ids(self):
        print('get channel subscriptions...')
        next_page_token = None
        url = f'https://youtube.googleapis.com/youtube/v3/subscriptions?part=snippet&maxResults=50&mine=true&key={self.api_key}&access_token={self.access_token}'
        self.subscriptions_ids = []
        
        data = self.get_request_data(url)
        for sub in data["items"]:
            self.subscriptions_ids.append(sub["snippet"]["resourceId"]["channelId"])

        next_page_token = data.get("nextPageToken")
        while True:
            next_page_url = f'https://youtube.googleapis.com/youtube/v3/subscriptions?part=snippet&maxResults=50&mine=true&pageToken={next_page_token}&key={self.api_key}&access_token={self.access_token}'
            data = self.get_request_data(next_page_url)
            for sub in data["items"]:
                self.subscriptions_ids.append(sub["snippet"]["resourceId"]["channelId"])

            # Check if there are more pages
            next_page_token = data.get("nextPageToken")

            # Exit the loop if there are no more pages
            if not next_page_token:
                break

        return self.subscriptions_ids
    
    # Get a channel's activities
    def get_channel_activities(self, channelId, maxResult):
        print('get channel activities...')
        url = f'https://www.googleapis.com/youtube/v3/activities?part=snippet,contentDetails&channelId={channelId}&maxResults={maxResult}&key={self.api_key}'
        data = self.get_request_data(url)
        self.activities = data
        return data


    # Get a categorie's title
    def get_category_title(self, categoryId):
        print('get category title...')
        url = f'https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&id={categoryId}&key={self.api_key}'
        data = self.get_request_data(url)
        self.activities = data
        return data 
    
    # Get a video's info
    def get_video_info(self, videoId):
        print('get video info...')
        url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={videoId}&key={self.api_key}'
        data = self.get_request_data(url)
        self.activities = data
        return data 