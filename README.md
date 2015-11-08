# Birdseed
## What is it?
`birdseed` is a utility to create pseudo and/or "real" random numbers from tweets based on a particular search query over Twitter's API. Use Twitter's noise to your advantage!

## What else?
**This is for fun. It's not secure. Don't use it in production :)**

It can be run in two modes: `real=True` and `real=False`. Real mode is default.

When run in real mode, `birdseed` will get up to 100 tweets for a particular search query, compute a hash for each tweet, and store these in a list. When the user calls `birdseed_instance.random()` the last hash will be popped off the hashes list. When the list of hashes is 0, Twitter's API will be called again for the given search query. *There's no guarantee though that tweets coming back are new and were not previously hashed and popped off. Ideally, use a search query with lots of entropy (something short like a single character: 'a', 'e', 'i', 'o', 'u')*

When run in non-real (pseudo) mode, `birdseed` will seed Python's random number generator with the first tweet it finds for the given search query.

The hash algorithm used is SHA224, with an input vector of the text of the tweet, the Twitter handle, and the timestamp. 

## Requirements
Python 2.7+ or Python 3.3+, pip, and Twitter App credentials 

## Installation
`pip install birdseed`

## Usage
```python
from __future__ import print_function

import birdseed
query = 'donald trump'
access_key = 'YOUR_ACCESS_KEY'
access_secret = 'YOUR_ACCESS_SECRET'
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'

t = birdseed.Birdseed(query, access_key, access_secret, consumer_key, consumer_secret)
print(t.random())
```

## Contributing
Pull requests are much appreciated and accepted.


## License
Released under the [MIT License](http://www.opensource.org/licenses/MIT)
