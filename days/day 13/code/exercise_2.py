def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:  # The error was that before it was 'year % 4000', however, to know if the year is in fact a leap year, you must divide it by 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap(2000))