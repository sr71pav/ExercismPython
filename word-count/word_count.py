import string
import re

def word_count(strin):
    res = {}
    strin = re.sub('[^A-Za-z0-9]', ' ', strin)
    strlist = string.split(strin.lower())
    for word in strlist:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res
