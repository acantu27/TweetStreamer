import argparse
import os
import settings
import sqlite3
import time

from pyfiglet import Figlet
from termcolor import colored
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from unidecode import unidecode


class MyStreamListener(StreamListener):
    """MyStreamListener: Inherited class from tweepy, StreamListener
    Used to overwrite on_status() and on_error()"""

    def on_status(self, status):
        """on_status: Overwrites StreamListener method
        Refer to tweepy & Twitter API documentation to explain why/how this was done to pull the full text from tweets
        'on_data' makes it difficult to pull tweets without being truncated"""
        try:
            if hasattr(status, 'retweeted_status'):
                try:
                    tweet = status.retweeted_status.extended_tweet["full_text"]
                except:
                    tweet = status.retweeted_status.text
            else:
                try:
                    tweet = status.extended_tweet["full_text"]
                except AttributeError:
                    tweet = status.text

            # Remove commas and new lines to prevent issues with CSV files
            tweet = tweet.replace(',', '')
            tweet = tweet.replace('\n', ' ')
            tweet = unidecode(tweet)

            username = status.user.screen_name
            date_time = status.created_at
            time_ms = status.timestamp_ms

            print(colored(time_ms, 'red'), colored(date_time, 'red'),
                  colored(username, 'yellow'), colored(tweet, 'blue'))

            stream_db.insert_into(time_ms, date_time, username, tweet)

        except KeyError as e:
            print(str(e))
        return True

    def on_error(self, status):
        """On Error: Prints error to console
        :param status: error code"""
        print("Error: ", status)

    def on_disconnect(self, notice):
        """on_disconnect: Prints notice to console
        :param notice: notice
        """
        print(notice)
        print("Disconnecting...")


class Database:
    def __init__(self, name):
        self.filename = name
        self.db_conn = sqlite3.connect(name)
        self.db_cur = self.db_conn.cursor()

    def create_table(self):
        try:
            self.db_cur.execute("CREATE TABLE IF NOT EXISTS twitter"
            "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "time_ms INTEGER NOT NULL, "
            "date_time REAL, "
            "username REAL NOT NULL, "
            "tweet REAL NOT NULL)")
            self.db_conn.commit()
        except Exception as e:
            print(str(e))

    def insert_into(self, time, date, user, tweet):
        self.db_cur.execute("INSERT INTO twitter (time_ms, date_time, username, tweet) VALUES (?, ?, ?, ?)",
                         (time, date, user, tweet))
        self.db_conn.commit()

    def close_db(self):
        self.db_conn.close()


argpar = argparse.ArgumentParser(prog='Tweet Streamer',
                                 usage='Script designed to stream tweets using specified keywords')
argpar.add_argument('-o', '--output', nargs='?', action='store', dest='output', default='output.db',
                    help='Saves tweets as specified output file name')
argpar.add_argument('-v', '--version', action='store_true', help='Displays programs current version')

args = argpar.parse_args()

if(args.version == True):
    print("Tweet Streamer 1.0")
    os._exit(1)

f = Figlet(font='slant')
print(f.renderText('Tweet Streamer'))
print('Use \'Ctrl + c\' to stop the stream\n')
print('Tweet Streamer will start in 5 seconds...')
time.sleep(5)

stream_db = Database(args.output)
stream_db.create_table()

try:
    while True:
        auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
        auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
        print(colored('STARTING TWEET STREAMER....', 'green'))
        print('Time (ms)\tDate Time\tUsername\tTweet')
        print('---------------------------------------------------------------')
        twitterStream = Stream(auth, MyStreamListener(), tweet_mode='extended')
        twitterStream.filter(languages=settings.SEARCH_LANG, track=settings.SEARCH_TERMS)
except Exception as e:
    print(str(e))
    time.sleep(5)
except KeyboardInterrupt:
    print(colored('Stop requested...', 'red'))
    print(colored('TERMINATING TWEET STREAM....', 'red'))
    stream_db.close_db()
    pass