from youtube_channel_videos_scraper_bot import *

youtube.login(username="alexandresimon3539",password="youtube password")
youtube.open("https://www.youtube.com/c/Thequint/videos")
all_data=[]
for i in range(0,5):
	response=youtube.channel_videos()
	data=response['body']
	all_data.extend(data)
print(all_data)