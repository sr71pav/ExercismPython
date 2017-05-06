import string

def is_pangram(teststr):
    tempstr = set(teststr.upper())

    for char in string.ascii_uppercase:
        if  not char in tempstr:
            return False
    return True
