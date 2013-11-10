#! -*- coding: utf-8 -*-
import pymongo
import codecs
from modules.Config import Config
import random

def pickup_hannya_tweet(word, tweets):
    count = tweets.count()
    if count == 0:
        return "%s: %s" % (word.encode("utf-8"), "None")

    tweet = tweets[random.randint(0,count-1)]
    return "%s: %d %s , other %d tweets" % (word.encode("utf-8"), tweet['id'], tweet['text'].encode('utf-8'), count)

def print_hannya(word, db=None):
    if not db:
        conn = pymongo.Connection()
        db = conn.hannya

    tweets = db.tweet.find({"word": word})
    print pickup_hannya_tweet(word, tweets)

if __name__ == "__main__":
    conn = pymongo.Connection()
    db = conn.hannya

    conf = Config()
    filename = conf.HANNYA_FILE
    with codecs.open(filename, 'r', 'utf-8') as f:
        for line in f:
            print_hannya(line[0], db)

