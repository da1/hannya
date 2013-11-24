from modules.db.hannya import Hannya

def uniq_tweets(tweets):
    utweets = {}
    for tweet in tweets:
        utweets[tweet['id']] = tweet
    return utweets 

def print_tweet(tweet):
    print "id:%s\tword:%s\ttext:%s" % (
            tweet['id'],
            tweet['word'].encode("utf-8"),
            tweet['text'].encode("utf-8"),
            )

def db_clear(db):
    db.drop()

if __name__ == "__main__":
    db = Hannya()

    tweets = db.find(None)
    utweets = uniq_tweets(tweets)
    db_clear(db)
    for tweet_id in utweets.keys():
        tweet = utweets[tweet_id]
        db.save(tweet['id'],
                tweet['word'].encode("utf-8"),
                tweet['text'].encode("utf-8"),
                )

