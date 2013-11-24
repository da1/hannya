# -*- coding: utf-8 -*-
import codecs
from modules.Config import Config

def hasHannya(text):
    ret = False
    word = ""
    conf = Config()
    filename = conf.HANNYA_FILE
    with codecs.open(filename, 'r', 'utf-8') as f:
        for line in f:
            line = line.rstrip()
            if text.find(line) >= 0:
                return ('', False)
            if text.find(line[0]) >= 0:
                ret = True
                word = line
    if len(word) > 0:
        return (word[0], ret)
    return (word, ret)

def hannyaFilter(texts):
    list = []
    for t in texts:
        w, has = hasHannya(t)
        if has:
            list.append((w, t))
    return list

