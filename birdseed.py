"""
Birdseed is a utility to create pseudo and/or "real" random numbers from tweets
based on a particular search query over Twitter's API. Use Twitter's noise to
your advantage!

This is for fun, it's not secure. Don't use it in production. :)
"""

__author__ = "Ryan McDermott (ryan.mcdermott@ryansworks.com)"
__version__ = "0.2.4"
__copyright__ = "Copyright (c) 2015 Ryan McDermott"
__license__ = "MIT"

import twitter
import hashlib
import random


class Birdseed():
    def __init__(self, query, access_key, access_secret, consumer_key,
                 consumer_secret, real=True):
        self.access_key = access_key
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.real = real
        self.query = query

        self._validate_init_args()

        # Create a list that will hold all of the hashes of the results from
        # the query
        self.hashes = []

        self.twitter = twitter.Twitter(auth=twitter.OAuth(self.access_key,
                                       self.access_secret, self.consumer_key,
                                       self.consumer_secret))

        if self.real:
            self.get_randomness(self.query)
        else:
            self.reseed(self.query)

    def _validate_init_args(self):
        """ Make sure all the constructor arguments were passed and are not
            None. """

        birdseed_args = {
            'access_key': self.access_key,
            'access_secret': self.access_secret,
            'consumer_key': self.consumer_key,
            'consumer_secret': self.consumer_secret,
            'query': self.query
        }

        # iterate through the keys of the dict
        # check that the value it represents is "truthy" (in this case, not
        # None)
        # if it IS None, raise a ValueError telling the caller it must provide
        # that argument
        for key in birdseed_args:
            if not birdseed_args[key]:
                raise ValueError('Please provide `{}`'.format(key))

    def _real_random(self):
        if len(self.hashes) == 0:
            self.get_randomness(self.query)

        if len(self.hashes) >= 1:
            rand_hash = self.hashes.pop()
            # Format hash as a floating point number < 1, just as Python's
            # pseudo random generator does
            return (int(rand_hash, 16) >> 171) * 0.0000000000000001
        else:
            raise ValueError('No results returned from API. Either the keys'
                             'are too stressed or the search term has no'
                             'results.')

    def _pseudo_random(self):
        return random.random()

    def _create_hash(self, result):
        """ Compute SHA224 hash based on concatenation of the creation time,
            the twitter handle and the text."""
        text = (result["created_at"].encode('utf-8') +
                result["user"]["screen_name"].encode('utf-8') +
                result["text"].encode('utf-8'))
        return hashlib.sha224(text).hexdigest()

    def random(self):
        """ Public method to get the random number based on if it's pseudo or
            real."""
        if self.real:
            return self._real_random()
        else:
            return self._pseudo_random()

    def get_randomness(self, query):
        """ Public method to gather 100 tweets based on a search query and
            compute their hashes and store them in an internal list."""
        if not self.real:
            raise ValueError('Class instance of Birdseed is being run as a'
                             'pseudo random number generator. Create a new'
                             'instance that is real.')

        query = self.twitter.search.tweets(q=query, count=100)
        self.hashes.extend([self._create_hash(result) for result
                           in query['statuses']])

    def reseed(self, query):
        """ Public method to seed Python's random number generator with the
            first tweet obtained from Twitter's API for a particular query."""
        if self.real:
            raise ValueError('Class instance of Birdseed is being run as a'
                             'real random number generator. Create a new'
                             'instance that is pseudo.')

        self.query = query

        # Perform a basic search https://dev.twitter.com/docs/api/1/get/search
        query = self.twitter.search.tweets(q=query)

        # Seed Python's random number generator with the first status found
        result = query["statuses"][0]
        seed = int(hashlib.sha224(self._create_hash(result)).hexdigest(), 16)
        random.seed(seed)
