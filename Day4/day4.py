import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer_choice = random.randint(0, 2)
rock_paper_scissor = [rock, paper, scissor]
if choice >= 3 or choice < 0 :
    print("Invalid number. Please try again")
else:
    print(rock_paper_scissor[choice])
    print("Computer chose:")
    print(rock_paper_scissor[computer_choice])
    if(choice == 2 and computer_choice == 0):
        print('You lose!')
    elif(choice == 0 and computer_choice == 2):
        print("You Win!")
    elif choice == computer_choice:
        print("It's a draw")
    elif choice <= computer_choice:
        print('You lose!')
    else :
        print("You win!")