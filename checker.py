#! -*- coding: utf-8 -*-
import pymongo
import codecs
from modules.Config import Config

def print_hannya(word, db=None):
    if not db:
        conn = pymongo.Connection()
        db = conn.hannya

    tweet = db.tweet.find_one({"word": word})
    if not tweet:
        print word.encode("utf-8"), "None"
    else:
        print word.encode("utf-8"), tweet['id'], tweet['text'].encode('utf-8')

if __name__ == "__main__":
    conn = pymongo.Connection()
    db = conn.hannya

    conf = Config()
    filename = conf.HANNYA_FILE
    with codecs.open(filename, 'r', 'utf-8') as f:
        for line in f:
            print_hannya(line[0], db)

