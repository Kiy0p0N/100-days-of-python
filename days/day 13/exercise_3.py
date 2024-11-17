# Old code
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 or number % 5 == 0:
#             print("FizzBuzz")
#         if number % 3 == 0:
#             print("Fizz")
#         if number % 5 == 0:
#             print("Buzz")
#         else:
#             print([number])

# New code
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print([number])

print(fizz_buzz(15))

# This code had several bugs:
# 1st - in the first 'if' the logical operator 'or' was being used, and when used, only one condition needs to be true for the code to be executed. In that case, the right thing to do is to use the logical operator 'and', which only executes when both comparisons are true.
# 
# 2nd - more than one 'if' was being used, instead of 'elif', so all 'if's were executed, checking numbers that had already been checked previously. The right thing to do was to use 'elif' after the first 'if'.