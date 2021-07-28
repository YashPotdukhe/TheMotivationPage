import tweepy
import time
import requests
import json


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def updateStatus():
    for quoteNum in range(len(quoteList)):
        api.update_status("\"" + quoteList[quoteNum]['text'] + "\"" + " - " + quoteList[quoteNum]['author'])
        time.sleep(60 * 60 * 24)

# Authenticate to Twitter
api_key = "YxXvMP0WR67DsbCmyS7jtBhjE"
api_secret = "GA5REhUgjF8YC4dtGHPcYY5ZDiIBkTK3M6mtQy6X3oSJVkWe06"
access_token = "1419689610452537344-Ac98Jyr20pWtunx2Fcb8FC2slPTGlu"
access_secret = "hhfhzjhaDgE1lE2bC7NJ9d8MMVbpCrC6zkNf8ktaPSb6v"


auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

# Create API object
api = tweepy.API(auth)

# api.update_status("Hello World")

response = requests.get('https://type.fit/api/quotes')
#converts json string into python object
quoteDump = json.dumps(response.json())
quoteList = json.loads(quoteDump)


updateStatus()