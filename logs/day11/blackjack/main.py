############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#import modules here
from replit import clear
from art import logo
import random

#Define functions below 

#Deal both user and computer a starting hand of 2 random card values with a function
def deal_card():
  """Returns a random card from from the deck named cards"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Detect when computer or user has a blackjack (10+11) by adding up the scores and checking for a 21 result
#The sum() function adds numbers in a list together
#Check wether the sum only contains 2 cards in the list and if there is an 11 amongst that list, return 0 to indicate blackjack score
#If there is an 11 and score is >21 remove it from the list and append a 1 instead
def score_calc(cards):
  """Provide 'cards' list as input to add them together and obtain the total score """
  if sum(cards) == 21 and len(cards) == 2:
    return 0 

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


#Create a function to compare the scores between PC and user to see who won, lost, or if it is a draw
def comparison(user_score, pc_score):
  if user_score == pc_score:
    return "It's a Draw"
  elif pc_score == 0:
    return "You lose. Opponent has a Blackjack!"
  elif user_score == 0:
    return "You win with a Blackjack!"
  elif user_score > 21:
    return "It's a bust. You lose."
  elif pc_score > 21:
    return "You win. Opponent went over."
  elif user_score > pc_score:
    return "You win!"
  else:
    return "You lose."
    
#Define functions above
  
def blackjack_game():
  print(logo)
  user_cards = []
  pc_cards = []
  game_over = False
  
  for _ in range(2):
    """Iterates 2 times to call deal card for user and pc and appends 2 random cards for each to their respective list"""
    user_cards.append(deal_card())
    pc_cards.append(deal_card())
  
  
  #Create a while loop to check for game_over boolean (False) and to continue to calculate the score until it becomes True
  #Loop will continue to iterate as long as user wants to continue to draw cards
  while not game_over:
      
    #Call score_calc() function to calculate scores 
    #Store respecive scores in a variable for the user's score and PC's score
    user_score = score_calc(user_cards)
    pc_score = score_calc(pc_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {pc_cards[0]}")
    
    #If PC or user has a score 0 or user score is >21, game ends via a boolean change to True (game_over)
    #Otherwise ask the user if they would like to get another card
    #If they don't game ends
    #Create a while loop to check for game_over boolean (False) and to continue to calculate the score until it becomes True
    if user_score == 0 or pc_score == 0 or user_score > 21:
      game_over = True
    else:
      additional_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if additional_card == "y":
        user_cards.append(deal_card())
        clear()
        print(logo)
      else:
        game_over = True
        clear()
        print(logo)
  
  
  #Create a while loop for PC to play once user is done
  #PC will continue to draw cards as long as initial score is != 0 and score <17
  while pc_score != 0 and pc_score < 17:
    pc_cards.append(deal_card())
    pc_score = score_calc(pc_cards)

  if pc_score == 0:
    pc_score = 21
  if user_score == 0:
    user_score = 21

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {pc_cards}, final score: {pc_score}")
  print(comparison(user_score,pc_score))
  print("")


  
#Ask the user if they would like to play another game of Blackjack 
#If so restart and reprint Blackjack logo otherwise end game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  clear()
  blackjack_game()
