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

    def get_channel_video_data(self):
        "Extract all video information of the channel"
        print('get video data...')
        channel_videos, channel_playlists = self._get_channel_content(limit=50)

        parts=["snippet", "statistics","contentDetails", "topicDetails"]
        for video_id in tqdm(channel_videos):
            for part in parts:
                data = self._get_single_video_data(video_id, part)
                channel_videos[video_id].update(data)

        self.video_data = channel_videos
        return channel_videos

    def _get_single_video_data(self, video_id, part):
        """
        Extract further information for a single video
        parts can be: 'snippet', 'statistics', 'contentDetails', 'topicDetails'
        """

        url = f"https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={self.api_key}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data['items'][0][part]
        except KeyError as e:
            print(f'Error! Could not get {part} part of data: \n{data}')
            data = dict()
        return data

    def _get_channel_content_per_page(self, url):
        """
        Extract all videos and playlists per page
        return channel_videos, channel_playlists, nextPageToken
        """
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        channel_videos = dict()
        channel_playlists = dict()
        if 'items' not in data:
            print('Error! Could not get correct channel data!\n', data)
            return channel_videos, channel_videos, None

        nextPageToken = data.get("nextPageToken", None)

        item_data = data['items']
        for item in item_data:
            try:
                kind = item['id']['kind']
                published_at = item['snippet']['publishedAt']
                title = item['snippet']['title']
                if kind == 'youtube#video':
                    video_id = item['id']['videoId']
                    channel_videos[video_id] = {'publishedAt': published_at, 'title': title}
                elif kind == 'youtube#playlist':
                    playlist_id = item['id']['playlistId']
                    channel_playlists[playlist_id] = {'publishedAt': published_at, 'title': title}
            except KeyError as e:
                print('Error! Could not extract data from item:\n', item)

        return channel_videos, channel_playlists, nextPageToken