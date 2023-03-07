#Import modules
from replit import clear
from art import logo, vs
from game_data import data
import random

#Call a random item/dictionary (account on instagram) from the imported list 'data'
def generate_account():
  '''Generates a random account from 'data' list and returns it as output'''
  insta_account = random.choice(data)
  return insta_account

  
#Define the function to call the game to play 
def play_game():
  print(logo)
  option_a = generate_account()
  a_followers = option_a['follower_count']
  score = 0

  #Continue to loop game until user's answer is incorrect
  while score >= 0:
    #Generate a random option b account from the list 'data'
    option_b = generate_account()
    b_followers = option_b['follower_count']
    if option_b == option_a or a_followers == b_followers:
      option_b = generate_account()
      b_followers = option_b['follower_count']
  
    #Print data in a formatted sentence for comparisson
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print(a_followers) #comment out
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")
    print(b_followers) #comment out

    #Ask user for input and assign it to the account's follower count
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice == 'A':
      choice = a_followers
    elif choice == 'B':
      choice = b_followers

    #Obtain the correct answer by comparing the follower count on accounts 'a' and 'b'
    if a_followers > b_followers:
      answer = a_followers
    else:
      answer = b_followers
  

    #Compare the user's choice to the correct answer and keep track of score by ending game if wrong answer or adding 1 
    if choice != answer:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      return
    elif choice == answer:
      score += 1
      clear()
      print(logo)
      print(f"You're right! Current score: {score}.")
      
    #Move option b to option a at the end if answer was correct. Otherwise game would have ended
    option_a = option_b
    a_followers = b_followers

#Call the game function
play_game()

#Ask the player wheather they would like to play again
again = input("Play again? Type 'Y' or 'N': ").upper()
if again == "Y":
  clear()
  play_game()
