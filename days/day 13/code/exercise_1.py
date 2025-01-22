def odd_or_even(number):
    if number % 2 == 0:  # Before it was 'if number % 2 = 0:', the error was to have just one equals sign, an equals (=) is to assign a value, to compare there must be two (==)
        return "This is an even number."
    else:
        return "This is an odd number."

print(odd_or_even(10))