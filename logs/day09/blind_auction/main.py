from replit import clear
from art import logo


bid_ends = False

bidders = {}

def highest_bidder(key, value):
  highest_bid = 0
  winner = ""
  for key in bidders:
    bid_amount = bidders[key]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = key
  print(f"The winner is {winner} with a bid of ${highest_bid}")
  
print(logo)
while bid_ends == False:
  #key for dictionary
  name = input("What is your name?: ")
  #value for dictionary
  bid = int(input("what is you bid?: $"))
  bidders[name] = bid

  
  
  cont = input("Are there any more bidders? Type 'yes' or 'no'.\n")
  if cont == "yes":
    clear()
  else:
    bid_ends = True
    highest_bidder(key=name, value=bid)
    
