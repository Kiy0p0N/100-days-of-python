def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True  # 2 and 3 are primes
    elif num % 2 == 0 or num % 3 == 0:
        return False  # eliminates multiples of 2 and 3

    # only checks numbers of the form 6k +/- 1 up to the square root of num
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6  # advances to the next number 6k +/- 1
    return True

