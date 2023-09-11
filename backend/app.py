from flask import Flask, request
from pyyoutube import Api
from pyyoutube import Client
from traceback import print_exc
from youtube_stats import YTStats
from authorizer import Authorizer
from utilities import *
from JSONReader import *
import secrets
import json

#app = Flask(__name__)

TOKEN_FILE = "token.txt"

authorizer = Authorizer(TOKEN_FILE, secrets.API_KEY, secrets.CLIENT_ID, secrets.CLIENT_SECRET)
ACCESS_TOKEN = authorizer.token

yt = YTStats(secrets.API_KEY, ACCESS_TOKEN)

subs_id = read_subs()
for id in subs_id:
    acts = yt.get_channel_activities(id, 3)
    writeJSONToFile("acts.txt", acts)
    print(read_acts())

#@app.get('/summary')
#def summary_api():
#    return


#if __name__ == "__main__":
    #app.run()