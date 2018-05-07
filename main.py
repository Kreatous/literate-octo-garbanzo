import sys, tweepy, json

auth = tweepy.OAuthHandler(consumer_key='V987DRZmMDTuGv8qXwpPDQ',
	consumer_secret='YRyMcRI9xjaGb6UG5B8WC8pMY0G5ATZ5n1ObO7uAjjo')

auth.set_Access_token(access_token_key='869223589-3zpYLDRAsuz6RgLqUmvdGFDrmDLGVg12XBRqZC4J',
	access_token_secret='ezkHcbBYfcmfH4Y9T6zhH4FHVxRQZhMsfiW1tFJZ0')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text