import pymongo

class Hannya:
    def __init__(self):
        self.conn = pymongo.Connection()
        self.db = self.conn.hannya

    def find(self, word):
        key = {} if word is None else {"word": word}
        return self.db.tweet.find(key)

    def remove(self, tweet):
        self.db.tweet.remove(tweet)

    def drop(self):
        self.db.tweet.drop()

    def save(self, id, word, text):
        """
        db = Hannya()
        db.save(id, word, text.encode("utf-8"))
        """
        self.db.tweet.save({
            "id"   : id,
            "word" : word,
            "text" : text,
            });

    def disconnect(self):
        self.conn.disconnect()

