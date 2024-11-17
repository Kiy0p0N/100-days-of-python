def compare_bid(bids):
    """Compares bids and prints the highest one"""
    name_highest_bid = ''
    highest_bid = 0

    for key in bids:
        if bids[key] > highest_bid:
            name_highest_bid = key
            highest_bid = bids[key]

    print(f'The winner is {name_highest_bid} with a bid of ${highest_bid}.')

print('Welcome to the secret auction program')

bidding_dictionary = {}

while True:
    name = input('What is your name? ')
    bid = float(input('What is your bid? $'))

    bidding_dictionary[name] = bid

    new_bid = input('Are there any other bidders? Type "yes" or "no".').lower()

    if new_bid == 'yes':
        print('\n' * 20)
    else:
        print('\n' * 20)
        compare_bid(bidding_dictionary)
        break
