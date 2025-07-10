import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]
prompt = "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
while True:
    choice = input(prompt)
    try:
        choice = int(choice)
        if choice in [0,1,2]:
            break
        else:
           print("Invalid choice") 
    except ValueError:
        print("Invalid choice")

print(choices[choice])
pc = random.randint(0,2)
print("Computer chose:")
print(choices[pc])
if choice == 0:
    if pc == 0:
        print("It's a draw")
    elif pc == 1:
        print("You lose")
    else:
        print("You win")
elif choice == 1:
    if pc == 0:
        print("You win")
    elif pc == 1:
        print("It's a draw")
    else:
        print("You lose")
elif choice == 2:
    if pc == 0:
        print("You lose")
    elif pc == 1:
        print("You win")
    else:
        print("It's a draw")
