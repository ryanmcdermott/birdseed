# Birdseed
## What is it?
`birdseed` is a utility to seed Python's random number generator with the first tweet it finds from Twitter's search API for a given search query. Use Twitter's noise to your advantage!


## What else?
This is for fun, it's not secure. Don't use it in production :)


## Requirements
Python 2.7+ or Python 3.3+, pip, and Twitter App credentials 


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
