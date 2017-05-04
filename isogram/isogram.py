import string

def is_isogram(str):
    # COnvert to uppercase to find upper and lower character repeats
    strlist = list(str.upper())

    # create empty list
    testlist = []

    # Check each character against all ascii uppercase characters
    for char in strlist:
        if (char in string.ascii_uppercase):
            # add to list if a letter
            testlist.append(char)

    # Get the set of characters in the list
    testset = set(testlist)

    # If length of the set and length of list are the same, is isogram
    if (len(testlist)==len(testset)):
        return True
    return False
