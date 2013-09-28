#! -*- coding: utf-8 -*-
from modules import util
from modules import hannya
import pymongo

def get_timeline():
    api = util.get_api()
    return api.home_timeline()

def hannyaTweetFilter(tweets):
    result = []
    for t in tweets:
        w, has = hannya.hasHannya(t.text)
        if has:
            result.append((w, t))
    return result

def _print_(word, tweet):
    print '-----'
    print tweet.id
    print word
    print tweet.text.encode("utf-8")
    print '-----'

if __name__ == "__main__":
    usedb = True
    if usedb:
        conn = pymongo.Connection()
        db = conn.hannya

    timeline = get_timeline()
    hannya_tweets = hannyaTweetFilter(timeline)
    for word, tweet in hannya_tweets:
        if usedb:
            db.tweet.save({
                "id": tweet.id,
                "word": word,
                "text": tweet.text.encode("utf-8"),
                })
        else:
            _print_(word, tweet)
    if usedb:
        conn.disconnect()
