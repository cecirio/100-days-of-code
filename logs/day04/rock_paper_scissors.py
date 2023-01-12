rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

game = [rock, paper, scissors]

print("What do you choose?")
choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors: \n"))


if choice >= 3 or choice < 0:
  print("You typed an invalid number. You lose.")
else:
  print(game[choice])

  computer_random = random.randint(0, 2)
  print(f"Computer chose: {game[computer_random]}")
    
  if choice == computer_random:
    print("Draw")
  elif choice == 0 and computer_random == 1:
    print("You lose")
  elif choice == 0 and computer_random == 2:
    print("You Win!")
  elif choice == 1 and computer_random == 0:
    print("You Win!")
  elif choice == 1 and computer_random == 2:
    print("You lose")
  elif choice == 2 and computer_random == 1:
    print("You Win!")
  elif choice == 2 and computer_random == 0:
    print("You lose")
    
