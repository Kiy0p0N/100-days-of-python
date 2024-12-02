print('Welcome to the tip calculator!')  # Welcome message for the tip calculator

# Get the total bill amount from the user
total = float(input('What was the total bill? $'))

while True:  # Loop until a valid tip percentage is entered
    tip = int(input('How much tip would you like to give, 10, 12 or 15? '))  # Get the tip percentage

    # Check if the entered tip is valid (10, 12, or 15)
    if tip == 10 or tip == 12 or tip == 15:
        break  # Exit the loop if the tip is valid
    else:
        print('Enter one of the optional values!')  # If invalid, ask the user to enter a valid tip
        continue  # Continue the loop to prompt for a valid input

# Get the number of people to split the bill
people = int(input('How many people to split the bill? '))

# Calculate the amount each person should pay
pay = (total + (total * (tip / 100))) / people

# Print the amount each person needs to pay, formatted to two decimal places
print(f'Each person should pay: ${pay:.2f}')
