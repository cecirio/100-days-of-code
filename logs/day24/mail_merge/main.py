PLACEHOLDER = "[name]"

with open("input/names/invited_names.txt") as guest_names:
    guest_list = guest_names.readlines()

  
with open("input/letters/starting_letter.txt") as empty_letter:
    letter = empty_letter.read()
    for guest in guest_list:
        stripped_guest = guest.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_guest)
        with open(f"output/ready_to_send/letter_for_{stripped_guest}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
