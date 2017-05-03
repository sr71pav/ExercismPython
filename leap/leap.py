def is_leap_year(year):
    # Check for div by 4
    if (year % 4 == 0):
        # Check for div by 100
        if (year % 100 == 0):
            # Check for div by 400
            if (year % 400 == 0):
                return True
        else:
            return True
    
    #Default to False
    return False