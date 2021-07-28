import tweepy
import time
import requests
import json


# Authenticate to Twitter
api_key = "YxXvMP0WR67DsbCmyS7jtBhjE"
api_secret = "GA5REhUgjF8YC4dtGHPcYY5ZDiIBkTK3M6mtQy6X3oSJVkWe06"
access_token = "1419689610452537344-Ac98Jyr20pWtunx2Fcb8FC2slPTGlu"
access_secret = "hhfhzjhaDgE1lE2bC7NJ9d8MMVbpCrC6zkNf8ktaPSb6v"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

# Create API object
api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '@TheMotivationP3' in tweet.full_text.lower():
            print(str(tweet.id) + '-' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " Keep working!", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)


#while True:
 #   reply()
  #  time.sleep(15)