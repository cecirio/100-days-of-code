alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(cipher_direction, input_text, shift_amnt):
  output_text = ""
  for letter in input_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      if cipher_direction == "encode":
        new_position = position + shift_amnt
      elif cipher_direction == "decode":
        new_position = position - shift_amnt
      output_text += alphabet[new_position]
    else:
      output_text += letter
  print(f"Here's the {cipher_direction}d result: {output_text}")

from art import logo
print(logo)


end_game = False
while end_game == False:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift %= 26
  
  caesar(cipher_direction=direction, input_text=text, shift_amnt=shift)

  choice = input("\nType 'yes' if you want to go again. Otherwise type 'no'. \n").lower()
  if choice == "no":
    end_game = True
    print("Goodbye!")
    
'''
def caesar(cipher_direction, input_text, shift_amnt):
  output_text = ""
  if cipher_direction == "decode":
    shift_amnt * -1
  for letter in input_text:
    position = alphabet.index(letter)
    new_position = position + shift_amnt
    output_text += alphabet[new_position]
  print(f"The {cipher_direction}d text is {output_text}")
'''

'''
def encrypt(plain_text, shift_amnt):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amnt
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")
    
def decrypt(cipher, shift_amnt):
  plain_text = ""
  for letter in cipher:
    position = alphabet.index(letter)
    new_position = position - shift_amnt
    new_letter = alphabet[new_position]
    plain_text += new_letter
  print(f"The decoded text is {plain_text}")
'''

'''
if direction == "encode":
  encrypt(plain_text=text, shift_amnt=shift)
elif direction == "decode":
  decrypt(cipher=text, shift_amnt=shift)
else:
  print("Invalid input. Try Again.")
'''
