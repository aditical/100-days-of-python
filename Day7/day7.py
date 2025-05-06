from Day7.main_game import game_start
from Day7.hangman_images import logo
 
print(logo)
print("!!!!!!!!! Guess the word below!!!!!!!!! \n")
game_start()
play_again = input("Do you want to play again? Type Y for Yes and N for No: ").lower()
print(play_again)
if(play_again == "y"):
    game_start()
else: 
    print("Okay, sure! See ya next time!")





