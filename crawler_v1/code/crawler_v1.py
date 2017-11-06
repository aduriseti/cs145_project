import tweepy
consumer_key = "51MI8RrYmzO4btCKG4Qb5uqAa"
consumer_secret = "ajpPv3Ag0NvMEQLBIwiPyDyU78BbLZn8IS1gTba4x9ZOHNPMNM"
access_token = "3004471069-VDbNpT9NO0QOtiqKZXkoH5Flv4MArCflIYImXjn"
access_token_secret = "sP6KMjPZXxYAnaae8bOiauLjCVnx8bzWkBk4KU1iZBxdl"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

n = 3 # Tweet count

### Basic API functionality

# # Print tweets from my home timeline
# for status in tweepy.Cursor(api.home_timeline).items(n):
#     # Process a single status
#     print(status.text)
# #     print(status._json)

# # Getting tweets from the New York Times user
# for tweet in api.user_timeline(id="nytimes", count=n):
#     # printing the text stored inside the tweet object
#     print(tweet.text)

# get tweets by keyword
tweets = api.search(q="stock", lang="en")
for tweet in tweets[:n]:
    # printing the text stored inside the tweet object
    print(tweet.user.screen_name,"Tweeted:",tweet.text)

import json
with open("sample_tweets.json", "w") as tweetfile:
    json.dump([tweet._json for tweet in tweets], tweetfile)
