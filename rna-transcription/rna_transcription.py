def to_rna(strin):
    for char in strin:
        if (char != 'G') and (char != 'C') and (char != 'A') and (char != 'T'):
            return ''
    strin = strin.replace('G','-')
    strin = strin.replace('C','G')
    strin = strin.replace('A','U')
    strin = strin.replace('T','A')
    strin = strin.replace('-','C')
    return strin
