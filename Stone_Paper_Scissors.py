import random
stone = """
    ______
---'  ____)
     (_____)
     (_____)
     (____)
---._(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
shapes= [stone, paper, scissors]
names = ["stone", "paper", "scissors"]

print("======= STONE PAPER SCISSORS =======")

user_input = input("Enter your choice (0=Stone, 1=Paper, 2=Scissors): ")
user_input = int(user_input)

computer_choice = random.randint(0, 2)

print("\nYou chose:")
print(shapes[user_input])

print("Computer chose:")
print(shapes[computer_choice])

if user_input == computer_choice:
    print("It's a DRAW!")
elif (user_input == 0 and computer_choice == 2) or \
     (user_input == 1 and computer_choice == 0) or \
     (user_input == 2 and computer_choice == 1):
    print("🏆 You WIN!")
else:
    print("💀 You LOSE!")