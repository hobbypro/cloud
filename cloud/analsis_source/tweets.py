import tweepy
from settings import *


class SearchedRecentTweetsSource:
    def __init__(self, keyword=""):
        self.keyword = keyword
        self.auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        self.auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

    def pull(self):
        api = tweepy.API(self.auth)
        searched_tweets = tweepy.Cursor(api.search, q=self.keyword).items(LIMIT_PULL_TWEETs)
        return '\n'.join([tweet.text for tweet in searched_tweets])
