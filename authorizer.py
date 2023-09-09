from pyyoutube import Api
from pyyoutube import Client
from traceback import print_exc
import webbrowser

class Authorizer:

    def __init__(self, TOKEN_FILE, API_KEY, CLIENT_ID, CLIENT_SECRET):
        try:
            self.client = Client(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        except:
            raise Exception("Client verification failed.")

        f = open(TOKEN_FILE, 'a+') #Creates the file if it doesn't exist
        f.close()

        self.token = self.readToken(TOKEN_FILE)

        # Try api authorization with file token OTHERWISE do url authorization
        try:
            if(self.token == ""): raise Exception("No token.")
            self.api = Api(api_key=API_KEY, access_token=self.token)
            self.api.get_subscription_by_me(mine=True, parts=["id","snippet"], count=1)
        except:
            self.token = self.url_auth()
            self.writeToFile(TOKEN_FILE, self.token.access_token)
            self.api = Api(api_key=API_KEY, access_token=self.token.access_token)

    def url_auth(self):
        webbrowser.open_new_tab(self.client.get_authorize_url()[0])
        response_url = input("Paste the response URL: ")
        return self.client.generate_access_token(authorization_response=response_url)

    def writeToFile(self, file, str):
        f = open(file, "w")
        f.write(str)
        f.close()

    def readToken(self, file):
        f = open(file, "r")
        token_tmp = f.read()
        return token_tmp

