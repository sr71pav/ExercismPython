def distance(strand1, strand2):
    if (len(strand1) != len(strand2)):
        raise ValueError
    count = 0
    for i in xrange(len(strand1)):
        if (strand1[i] != strand2[i]):
            count+=1
    return count
