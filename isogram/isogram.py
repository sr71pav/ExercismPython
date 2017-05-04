def is_isogram(str):
    setstr = set(str)
    lisstr = list(str)
    if (len(setstr)==len(lisstr)):
        return True
    return False
