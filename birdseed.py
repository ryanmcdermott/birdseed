"""
Birdseed is a utility to create pseudo and/or "real" random numbers from tweets based 
on a particular search query over Twitter's API. Use Twitter's noise to your advantage!

This is for fun, it's not secure. Don't use it in production :)
"""

__author__ = "Ryan McDermott (ryan.mcdermott@ryansworks.com)"
__version__ = "0.2.3"
__copyright__ = "Copyright (c) 2015 Ryan McDermott"
__license__ = "MIT"

from twitter import *
import hashlib
import random

class Birdseed():
    def __init__(self, query, access_key, access_secret, consumer_key, consumer_secret, real=True):
        self.access_key = access_key
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.real = real
        self.query = query

        # Create a list that will hold all of the hashes of the 
        self.hashes = []

        if self.access_key == None or self.access_secret == None or self.consumer_key == None or self.consumer_secret == None:
            raise ValueError('Please provide all of the following: access_key, access_secret, consumer_key, consumer_secret')
        else:
            self.twitter = Twitter(auth = OAuth(self.access_key, self.access_secret, self.consumer_key, self.consumer_secret))

        if query == None:
            raise ValueError('Please provide a search query')

        if self.real: 
            self.get_randomness(self.query)
        else:
            self.reseed(self.query)


    def _real_random(self):
        if len(self.hashes) == 0:
            self.get_randomness(self.query)

        rand_hash = self.hashes.pop()
        # Format hash as a floating point number < 1, just as Python's pseudo random generator does.
        return (int(rand_hash, 16) >> 171) * 0.0000000000000001


    def _pseudo_random(self):
        return random.random()


    def _create_hash(self, result):
        """ Computer SHA224 hash based oncatenation of the creation time, the twitter handle and the text."""
        text = result["created_at"].encode('utf-8') + result["user"]["screen_name"].encode('utf-8') + result["text"].encode('utf-8')
        return hashlib.sha224(text).hexdigest()


    def random(self):
        """ Public method to get the random number based on if it's pseudo or real"""
        if self.real:
            return self._real_random()
        else:
            return self._pseudo_random()


    def get_randomness(self, query):
        """ Public method to gather 100 tweets based on a search query and computer their hashes and store them in an internal list"""
        if self.real == False:
            raise ValueError('Class instance of Birdseed is being run as a pseudo random number generator. Create a new instance that is real')

        query = self.twitter.search.tweets(q=query, count=100)

        for result in query["statuses"]:
            self.hashes.append(self._create_hash(result))


    def reseed(self, query):
        """ Public method to seed Python's random number generator with the first tweet obtained from Twitter's API for a particular query"""
        if self.real == True:
            raise ValueError('Class instance of Birdseed is being run as a real random number generator. Create a new instance that is pseudo')

        self.query = query
        
        # Perform a basic search 
        # https://dev.twitter.com/docs/api/1/get/search
        query = self.twitter.search.tweets(q = query)

        # Seed Python's random number generator with the first status found.
        result = query["statuses"][0]
        seed = int(hashlib.sha224(self._create_hash(result)).hexdigest(), 16)
        random.seed(seed)
