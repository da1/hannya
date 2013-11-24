#! -*- coding: utf-8 -*-
from modules import util
from modules import hannya
from modules.db.hannya import Hannya

TWEET_LIMIT = 100

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
        db = Hannya()

    timeline = get_timeline()
    hannya_tweets = hannyaTweetFilter(timeline)
    for word, tweet in hannya_tweets:
        if usedb:
            tweets = db.find(word).sort("id")
            if tweets.count() > TWEET_LIMIT:
                tweet_one = tweets[0]
                db.remove(tweet_one)
            db.save(
                tweet.id,
                word,
                tweet.text.encode("utf-8"),
                )
        else:
            _print_(word, tweet)
    if usedb:
        db.disconnect()

