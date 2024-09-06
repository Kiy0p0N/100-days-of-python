print('Welcome to the tip calculator!')

while True:
    try:
        total = float(input('What was the total bill? $'))
        break
    except ValueError:
        print('This input is invalid')
        continue

while True:
    try:
        tip = int(input('How much tip would you like to give, 10, 12 or 15? '))

        if tip ==10 or tip == 12 or tip == 15:
            break
        else:
            print('Enter one of the optional values!')
            continue
        
    except ValueError:
        print('This input is invalid!')
        continue
    
    
while True:
    try:
        people = int(input('How many people to split to bill? '))
        break
    except ValueError:
        print('This input is invalid!')
        continue


pay = (total + (total * (tip / 100))) / people

print(f'Each person should pay: ${pay:.2f}')