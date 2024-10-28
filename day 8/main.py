# Main function to perform Caesar cipher encoding or decoding
def caesar(decode_or_encode):
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))
    
    caesar_text = ''

    # Reverses the shift for decoding
    if decode_or_encode == 'decode':
        shift *= -1

    # Loops through each letter in the text
    for letter in text:
        # Adds any non-alphabet character directly to the result
        if letter not in alphabet:
            caesar_text += letter

        # Shifts alphabet letters based on the shift number
        else:
            shifted_position = alphabet.index(letter) + shift
            shifted_position %= len(alphabet)
            caesar_text += alphabet[shifted_position]

    print(f'Here is the {decode_or_encode}d result: {caesar_text}')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Main loop allowing multiple encodings or decodings
while True:
    direction = input('Type "encode" to encrypt or type "decode" to decrypt:\n').lower()

    # Validates the choice and calls the Caesar function if valid
    if direction == 'encode' or direction == 'decode':
        caesar(direction)
        again = input('Type "yes" if you want to go again. Type anything else to get out.\n').lower()
        if again != 'yes':
            print('Bye.')
            break
    else:
        print('Do not have this option.')