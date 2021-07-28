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

hashtag = '#MotivationalQuote'
tweetNum = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNum)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(60*60*5)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(60*60*5)

searchBot()