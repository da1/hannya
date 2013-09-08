#! -*- coding: utf-8 -*-
from modules import util
from modules import hannya

def get_timeline():
    api = util.get_api()
    return api.home_timeline()

def get_text(tweets):
    return [ t.text for t in tweets ]

if __name__ == "__main__":
    timeline = get_timeline()
    hannya_texts = hannya.hannyaFilter(get_text(timeline))
    for i in hannya_texts:
        print '-----'
        print i[0].encode("utf-8")
        print '-'
        print i[1].encode("utf-8")
        print '-----'
