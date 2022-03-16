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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_list[user_choice])
print("Computer Choice:")
pc_choice = random.randint(0,2)
print(game_list[pc_choice])

if user_choice == 0 and pc_choice == 1:
    print("You Win!")
elif user_choice == 0 and pc_choice == 2:
    print("You Win!")
elif user_choice == 1 and pc_choice == 0:
    print("You Loose!")
elif user_choice == 1 and pc_choice == 2:
    print("You Loose!")
elif user_choice == 2 and pc_choice == 0:
    print("You Loose!")
elif user_choice == 2 and pc_choice == 1:
    print("You Win!")
elif user_choice == pc_choice:
    print("DRAW!, Try Again.")

