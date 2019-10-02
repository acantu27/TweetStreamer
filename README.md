# Tweet Streamer
![License](https://img.shields.io/badge/license-MIT%20License-lightgrey.svg "License") ![Version](https://img.shields.io/badge/version-1.1-blue.svg)

Tweet Streamer is a script designed to stream and save tweets for data analysis.

#### Preview:
![Tweet Streamer Preview][preview]

## Introduction
Tweet Streamer is a python script utilizing Twitter's streaming API. It streams **live** tweets and saves their properties. Tweets are able to be filtered based on desired keywords or languages.

## Requirements
* Please see [`requirements.txt`](https://github.com/acantu27/TweetStreamer/blob/master/requirements.txt) for the necessary dependencies
* Requires Python 3+
* Some features might not be supported such as colored text output

## Usage
1. Clone the repository to the desired location.

2. [Register an account with Twitter to generate your API key][1]. 

3. The setup guide should automatically run the first time. Alternatively you can run `tweetstreamer.py -s` to relaunch the setup. Or you can manually insert your credentials into the [`settings.py`](https://github.com/acantu27/TweetStreamer/blob/master/tweetstreamer/settings.py) file.

    *Note: All values in the `settings.py` act as the default values.*
```python
CONSUMER_KEY = 'consumer_key_here'
CONSUMER_SECRET = 'consumer_key_here'
ACCESS_TOKEN = 'access_token_here'
ACCESS_SECRET = 'access_secret_here'
```
Tweet Streamer utilizes command line arguments. See help for more information `tweetstreamer.py -h`
```bash
optional arguments:
  -h, --help            show this help message and exit
  -o [OUTPUT], --output [OUTPUT]
                        Saves tweets as specified file name
  -t, --terse           Disables outputting tweets to console
  -c, --color           Enables colored text in console
  -v VERSION, --version VERSION
                        Displays current version
  -k KEYWORDS [KEYWORDS ...], --keywords KEYWORDS [KEYWORDS ...]
                        Filter tweets by the specified keywords
  -l LANGUAGES [LANGUAGES ...], --language LANGUAGES [LANGUAGES ...]
                        Filter tweets by the specified language.
  -s, --setup           Begins the setup process
```


A `KeyboardInterrupt` such as `Ctrl + C` will stop the stream and close the database if desired.

[1]: https://developer.twitter.com/
[preview]: images/preview.gif "Tweet Streamer Preview"
