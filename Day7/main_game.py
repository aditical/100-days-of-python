import random
from Day7.hangman_images import life_stages
from Day7.hangman_images import trophy
from Day7.hangman_images import logo
from Day7.words_list import array_of_words

def game_start():
    step = 0
    guess = len(life_stages)
    random_index = random.randint(0,len(array_of_words) - 1) 
    word_to_be_guessed = (array_of_words[random_index]).lower() 
    word_array = []
    guessed_letters = []
    length_of_word = len(word_to_be_guessed) 
    for number in range(length_of_word):
        word_array.append("_") 
    print(*word_array)
    print("\n")
    while guess > 0 and step < length_of_word:
        input_guessed_by_user = input("Guess a letter: \n").lower()
        occurance_of_letter = []
        if len(input_guessed_by_user) != 1:
            print("Invalid input! Please try again!\n")
        elif input_guessed_by_user in guessed_letters:
            print("You have already guessed the letter")
        else:
            guessed_letters.append(input_guessed_by_user)
            for number in range(length_of_word):
                if input_guessed_by_user == word_to_be_guessed[number]:
                    occurance_of_letter.append(number)
                    word_array[number] = input_guessed_by_user.lower()
                    step += 1
                    print(*word_array)
            if step == length_of_word:
                print(f"YOU HAVE WON THE GAME! WOHOOOOO {trophy}\n")
                break
            if input_guessed_by_user not in word_array:
                guess -= 1 
                print(life_stages[guess])
                print(*word_array)
                if guess == 0 :   
                    print(f"The word was {word_to_be_guessed}\n")
                    break