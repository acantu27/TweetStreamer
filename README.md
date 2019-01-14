# Tweet Streamer
Tweet Streamer is a script designed to stream and save untruncated tweets with the specified keywords.

#### Preview:
![Tweet Streamer Preview][preview]

## Introduction
Tweet Streamer is a python script built using Tweepy <sup>[1][1]</sup>. It streams **_live_** tweets and saves them to a database. Tweets are able to be filtered based on desired keywords or languages. This provides a large amount of data for Machine Learning or Data Science projects.

## Requirements
* Please see `requirements.txt` for the necessary dependencies
* Requires Python 3+
* Some features won't on Windows system such as the colored text

## Usage
Clone the repository to the desired location. <sup>[2][2]</sup>

Register an account with Twitter to generate your API key <sup>[3][3]</sup>. Insert your credentials into the `settings.py` file.
```python
CONSUMER_KEY = 'consumer_key_here'
CONSUMER_SECRET = 'consumer_key_here'
ACCESS_TOKEN = 'access_token_here'
ACCESS_SECRET = 'access_secret_here'
```

Fill out the rest of the information in the `settings.py` file. `SEARCH_TERMS` specifies which keywords to filter for. If you desire no filters then leave the default values. `SEARCH_LANG` filters tweets based off the language specified. 
```python
SEARCH_TERMS = ["a", "e", "i", "o", "u"]
SEARCH_LANG = ["en"]
```
Tweet Streamer utilizes command line arguments.
```bash
python3 tweetstreamer.py [-h] [-o] [FILE]
-o, --output      Saves tweets as the specified output file name      DEFAULT='output.db'
-h, --help        Shows this help message and exits
-v, --version     Displays programs current version
```

Initialize the stream and save with the default values.
```bash
python3 tweetstreamer.py
```

Initialize the stream and save with the specified file name `tweet_stream.db`.
*Note: Output file must be a database (*.db) file.*
```bash
python3 tweetstreamer.py -o tweet_stream.db
```

A `KeyboardInterrupt` such as `Ctrl + C` will stop the stream and close the database if desired.

## References
1. [Tweepy Official Website](http://www.tweepy.org/)
2. [Github Documentation Cloning Repository](https://help.github.com/articles/cloning-a-repository/)
3. [Twitter API Registration Documents](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html)

[1]: http://www.tweepy.org/
[3]: https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html
[2]: https://help.github.com/articles/cloning-a-repository/
[preview]: images/preview.gif "Tweet Streamer Preview"
