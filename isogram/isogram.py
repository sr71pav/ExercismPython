def is_isogram(str):
    setstr = set(str.upper())
    lisstr = list(str.upper())
    if (len(setstr)==len(lisstr)):
        return True
    return False
