def is_isogram(str):
    str=str.replace(' ','')
    setstr = set(str.upper())
    lisstr = list(str.upper())
    if (len(setstr)==len(lisstr)):
        return True
    print setstr
    print lisstr
    return False
