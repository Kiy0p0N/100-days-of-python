def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Main function that performs the selected operation
def perform_operation(num1):
    # Prompt the user to choose an operation
    operation = str(input('Choose the operation:\n'
                          '+\n'
                          '-\n'
                          '*\n'
                          '/\n'
                          ''))
    # Get the second number for the operation
    num2 = float(input('Enter the second number: '))

    # Retrieve and execute the function corresponding to the chosen operation
    result = operation_functions[operation](num1, num2)

    print(f'{num1} {operation} {num2} = {result}')
    # Ask the user if they want to continue or end the session
    again = input(f'Type "y" to continue calculating with {result}, "n" to start a new calculation, or "s" to stop the session: ').lower()

    # If the user chooses to continue, call the function again with the current result
    if again == 'y':
        return perform_operation(result)  # Continue with the current result
    elif again == 'n':
        # Signal to start a new calculation
        return True
    else:
        # Stop the calculator session
        return False

operation_functions = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

print('Welcome to the Calculator')
# Main loop to keep the calculator running as long as the user wants
while True:
    # Get the first number to start the operation
    number01 = float(input('\nEnter the first number: '))

    # Call the operation function and update `continue_operation`
    continue_operation = perform_operation(number01)

    # If `continue_operation` is False, break the loop to stop the session
    if not continue_operation:
        break