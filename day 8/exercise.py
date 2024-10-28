def letter_true(name):
    total_love = 0

    for actual_letter in 'true':

        for letter in name:
            if letter == actual_letter:
                total_love += 1
            else:
                continue

    return total_love

def letter_love(name):
    total_love = 0

    for actual_letter in 'love':

        for letter in name:
            if letter == actual_letter:
                total_love += 1
            else:
                continue

    return total_love

def calculate_love_score(name1, name2):
    print(f"{letter_true(name1) + letter_true(name2)}{letter_love(name1) + letter_love(name2)}")
    
    
    
calculate_love_score()