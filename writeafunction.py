def is_leap(year):
    leap = False
    if year % 400 is 0:
        return True
    elif year % 4 is 0:
        if year % 100 is not 0:
            return True
        else:
            return False
    return False


    return leap

year = int(raw_input())
print is_leap(year)
