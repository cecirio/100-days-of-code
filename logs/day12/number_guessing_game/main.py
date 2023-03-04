#1. Import modules
import random
from art import logo

#2. Create constants for the number of lives left based on the difficulty selected
EASY_DIFF = 10
HARD_DIFF = 5

#8. Define a function that will take user's input 'easy' or 'hard'
# to return the appropriate constant as output which can be stored in a variable within another function
# This function's output will either be a 10 or a 5
def get_difficulty():
    """Based on the difficulty function will set the number of lives"""
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diff == "easy":
        return EASY_DIFF
    elif diff == "hard":
        return HARD_DIFF

#13. Define a function to check the user's guess with the generated number and subtract a life if 
# the guess is not equal to the generated number to set it as the return value to keep track in the
# game's while loop
def check_result(guess, number, lives):
    if guess > number:
        print("Too high.")
        return lives - 1
    elif guess < number:
        print("Too low.")
        return lives - 1
    else:
        print(f"You got it! The answer was {number}.")
   

#3. Define game function
def play_game():
  #4. Print the game's logo, welcome, and number guessing range
  print(logo)
  print("Welcome to The Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  #5. Create a variable to store a randomly generated number
  number = random.randint(1, 100)
  #6. Print generated number for testing purposes
  #print(f"psst the number is: {number}")

  #7. Ask the player for the desired difficulty to store the number of lives
  # in a variable that can be modified depending on number of tries left
  # Because this function will output a 10 or a 5 (number of lives based on difficulty)
  # the output needs to be stored in a variable in order for it to be used or modified later on
  lives = get_difficulty()

  #9. The game will continue until the number is guessed correctly unless the lives run out first.
  # There is no guess yet so there is an empty 'guess' variable to start.
  
  guess = ""
  while guess != number:
    #10. Start by keeping track of the remaining attempts in the game.
    print(f"You have {lives} attempts remaining to guess the number.")
    #11. Ask user for an integer input
    guess = int(input("Make a guess: "))
    
    #12. Keep track of the number of lives by checking the result of the guess 
    lives = check_result(guess,number,lives)
    #14. Player will be notified if the lives have run out and game will end via return statement.
    # Otherwise it will prompt the player to guess again and while loop will restart as long as 
    # guess number is not equal to the generated number
    if lives == 0:
        print("You've run out of guesses, you lose.")
        return
    elif guess != number:
        print("Guess again.")

#15. Call the game function to run the program
play_game()
