from flask import Flask, request
from pyyoutube import Api
from pyyoutube import Client
from traceback import print_exc

app = Flask(__name__)

TOKEN_FILE = "token.txt"
API_KEY = "[Your API Key]"
CLIENT_ID = "[Your client ID]"
CLIENT_SECRET = "[Your Client Secret]"

authorizer = Authorizer(TOKEN_FILE, API_KEY, CLIENT_ID, CLIENT_SECRET)

r = authorizer.api.get_playlists(
        channel_id="UCSoAKExYfolVOhB80ftPiYQ")
print(r.items)

r = authorizer.api.get_playlist_items(
        playlist_id="PLo4tTf0XUP0VYTo3PrJldqFOKjmhVGJUB")
print(r.items.contentDetails.videoId)




@app.get('/summary')
def summary_api():
    return


if __name__ == "__main__":
    app.run()