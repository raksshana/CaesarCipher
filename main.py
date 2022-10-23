import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      if cipher_direction == "encode":
        new_position = position + shift_amount 
        chosen_option = "encoded"
      elif cipher_direction == "decode":
        new_position = position - shift_amount 
        chosen_option = "decoded"
      new_letter = alphabet[new_position]
      end_text += new_letter
    else: 
      end_text += char

  print(f"The {chosen_option} text is: {end_text}")
  

caesar(text, shift, direction)

