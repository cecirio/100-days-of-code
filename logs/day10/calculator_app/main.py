from replit import clear
from art import logo

def add(n1, n2):
  """Add two numbers in parameter together."""
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}

def calculator():
  print(logo)
  end = False
  num1 = float(input("What is the first number?: "))
  
  for operator in operations:
    print(operator)
  
  while end == False:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    
    calculation = operations[operation_symbol]
    answer = calculation(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ").lower()
    if choice == "y":
      num1 = answer
    else:
      end = True
      clear()
      calculator()

calculator()
