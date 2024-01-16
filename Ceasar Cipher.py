
#Given
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#My take
if direction == "encode":
    def encrypt (plain_text, shift_number):
        print(f'plain_text = {text}' )
        print(f'shift number = {shift}')
        for char in plain_text:
            if char in alphabet:
                alphaindex = alphabet.index(char)
                ciphered_index = shift_number + alphaindex
                ciphered_text = alphabet[ciphered_index]
                print(ciphered_text, end = '')
    encrypt(plain_text = text, shift_number = shift)

elif direction == "decode":
    def decrypt (ciphered_text, shift_number):
        print(f'ciphered_text = {text}')
        print(f'shift number = {shift}')
        for char in ciphered_text:
            if char in alphabet:
                alphaindex = alphabet.index(char)
                plain_index = alphaindex - shift_number
                plain_text = alphabet[plain_index]
                print(plain_text, end = '')
    decrypt(ciphered_text = text, shift_number = shift)

#Course take
if direction == "encode":
    def encrypt(plain_text, shift_amount):
      cipher_text = ""
      for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
      print(f"The encoded text is {cipher_text}")
    encrypt(plain_text=text, shift_amount=shift)

elif direction == "decode":
    def decrypt(cipher_text, shift_amount):
        plain_text = ""
        for letter in cipher_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            plain_text += alphabet[new_position]
        print(f"The decoded text is {plain_text}")
    decrypt(cipher_text=text, shift_amount=shift)

#Course answer 2
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)




