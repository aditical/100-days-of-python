import random
import string
letters = string.ascii_letters
symbols = string.punctuation
numbers = string.digits
letter_array = []
symbols_array = []

print("Welcome to the PyPassword Generator!")
no_of_letters = input("How many letters would' you like in your password?\n")
no_of_symbols = input("How many symbols would you like?\n")
no_of_numbers = input("How many numbers would you like?")

for numbers in range(0, int(no_of_letters)):
    random_index = random.randint(0,len(letters) )
    random_letter = letters[random_index]
    letter_array.append(random_letter)

for numbers in range(0, int(no_of_symbols)):
    random_index_symbol = random.randint(0,len(symbols) )
    random_symbol = symbols[random_index_symbol]
    letter_array.append(random_symbol)

for numbers in range(0, int(no_of_numbers)):
    random_number = random.randint(0, 9)
    letter_array.append(random_number)

shuffled_array = random.sample( letter_array, len(letter_array) )
print(letter_array)
print(shuffled_array)
print(f"Your password is: {shuffled_array}")
password = ''
for letters in shuffled_array:
    password = (f"{password}{letters}")    
print(password)