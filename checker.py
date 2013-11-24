#! -*- coding: utf-8 -*-
import codecs
from modules.Config import Config
from modules.db.hannya import Hannya
import random

def pickup_hannya_tweet(word, tweets):
    count = tweets.count()
    if count == 0:
        return "%s: %s" % (word.encode("utf-8"), "None")

    tweet = tweets[random.randint(0,count-1)]
    return "%s: %d %s , other %d tweets" % (word.encode("utf-8"), tweet['id'], tweet['text'].encode('utf-8'), count)

def print_hannya(word, db=None):
    if not db:
        db = Hannya()

    tweets = db.find(word)
    print pickup_hannya_tweet(word, tweets)

if __name__ == "__main__":
    db = Hannya()

    conf = Config()
    filename = conf.HANNYA_FILE
    with codecs.open(filename, 'r', 'utf-8') as f:
        for line in f:
            print_hannya(line[0], db)

