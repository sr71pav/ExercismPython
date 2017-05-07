import string

def is_isogram(str):
    # Prefer not to execute str.upper() for every iteration
    str = str.upper()

    # create empty list
    testlist = []

    # Check each character against all ascii uppercase characters
    for char in str:
        if (char in string.ascii_uppercase):
            # add to list if a letter
            testlist.append(char)

    # Get the set of characters in the list
    testset = set(testlist)

    # If length of the set and length of list are the same, is isogram
    return len(testlist)==len(testset)
