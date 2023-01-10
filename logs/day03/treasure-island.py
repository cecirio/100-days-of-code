print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("\nYou are stranded on an island after a shipwreck. The night is dark and cold.")
print("Find shelter, but keep an eye out for the treasure! \nAhead of you is a dense jungle and a cross road. \n ")
path = input("Type \"left\" to follow the path that leads to an ominous sound.\nType \"right\" to take the path that leads to a faint gleam in the distance.\n").lower()

if path == "left":
  print("\nCLUE FOUND: Orange Broken lock")
  print("You follow the sound and reach a wide river. \nEven in the darkness you can see what looks like a temple on the other side.")
  print("You hear footsteps behind you. Quick!")
  print("")
  river = input("Type \"swim\" to swim across. \nType \"wait\" to wait for a piece of drift wood. \n").lower()
  if river == "wait":
    print("\nCLUE FOUND: Green Broken Lock")
    print("It was just a Jaguar cub! You pet the cub and hop on to the piece of drift wood.")
    print("You make it across safely. Inside the temple you find three out of five treasure chests left.")
    print("One red, one yellow, and one blue. Only one has the treasure. Which do you choose? \n ")
    color = input("Type \"red\", \"yellow\", or \"blue\". \n").lower()
    if color == "yellow":
      print("\nYou found the treasure! \nYou Win!")
    elif color == "red":
      print("\nYou set off a trap! You caught on fire. \nGame Over!")
    elif color == "blue":
      print("\nYou set off a trap! You were shot by arrows. \nGame Over!")
    else:
      print("\nNot a valid answer, cannibals followed your tracks and found you. \nGame Over!")
  elif river == "swim":
    print("\nYou were attacked by a caiman. \nGame Over!")
  else:
    print("\nNot a valid answer, You stepped on a twig and attracted a jaguar to your location. \nGame Over!")
elif path == "right":
  print("\nYou ran into cannibals. \nGame Over!")
else:
  print("\nNot a valid answer, You were caught by an anaconda. \nGame Over!")
