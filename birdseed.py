"""
Birdseed is a utility to seed Python's random number generator with the 
first tweet it finds from Twitter's search API for a given search query.

This is for fun, it's not secure. Don't use it in production :)
"""

__author__ = "Ryan McDermott (ryan.mcdermott@ryansworks.com)"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2015 Ryan McDermott"
__license__ = "MIT"

from twitter import *
import hashlib
import random

class Birdseed():
    def __init__(self, query, access_key, access_secret, consumer_key, consumer_secret):
        self.access_key = access_key
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.reseed(query)


    def random(self):
        return random.random()


    def reseed(self, query):
        self.query = query
        if self.access_key == None or self.access_secret == None or self.consumer_key == None or self.consumer_secret == None:
            raise ValueError('Please provide all of the following: access_key, access_secret, consumer_key, consumer_secret')
        else:
            twitter = Twitter(auth = OAuth(self.access_key, self.access_secret, self.consumer_key, self.consumer_secret))

        #-----------------------------------------------------------------------
        # perform a basic search 
        # Twitter API docs:
        # https://dev.twitter.com/docs/api/1/get/search
        #-----------------------------------------------------------------------
        query = twitter.search.tweets(q = query)

        #-----------------------------------------------------------------------
        # Grab the first status, concatenate the creation time, the twitter handle,
        # and the text. Use this in a SHA224 hash to seed Python's random number generator
        #-----------------------------------------------------------------------
        for result in query["statuses"]:
            text = result["created_at"].encode('utf-8') + result["user"]["screen_name"].encode('utf-8') + result["text"].encode('utf-8')
            seed = int(hashlib.sha224(text).hexdigest(), 16)
            random.seed(seed)
            break
