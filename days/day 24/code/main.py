# The objective is to create invitations automatically

with open('./input/letters/starting_letters.txt') as starting_letters:  # Open the file
    invited = starting_letters.read()  # Stores the text in the variable

with open('input/names/invited_names.txt') as invited_names:
    for name in invited_names:  # For each name in invited_names
        guest_name = name.split()[0]  # Transforms it into a list and takes the first element, the name

        birthday_invitation = invited.replace('[name]', guest_name)  # Change [name] in the invitation to the guest's name

        # Specifies the path to create and save the file, each file has a different name, depending on the guest
        path = f'./output/readyToSend/invitation-to-{guest_name.lower()}.txt'
        with open(path, mode='w') as invitation:
            invitation.write(birthday_invitation)