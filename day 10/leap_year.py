def is_leap_year(year):
    '''
    check if the year is a leap year
    '''

    # on every year that is divisible by 4 with no remainder
    if year % 4 == 0:
        # except every year that is evenly divisible by 100 with no remainder
        if year % 100 == 0:
            # unless the year is also divisible by 400 with no remainder
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

    else:
        return False

leap_year = int(input('Write the year for check if is leap or not leap.\n'))

print(is_leap_year(leap_year))