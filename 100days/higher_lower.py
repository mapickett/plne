import art
import hl_data
import random

def play_game(A, B):
    print('\n' * 25)
    print(art.higher_lower)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(art.vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    while True:
        choice = input("Who has more followers? Type 'A' or 'B': ")
        if choice in ['A', 'B']:
            break
    if choice == 'A':
        if A['follower_count'] > B['follower_count']:
            # correct answer
            new_element = hl_data.data.pop(random.randint(0,len(hl_data.data) - 1))
            return 1 + play_game(A, new_element)
        else:
            print("Sorry, that's wrong.")
            return 0
    else:
        if B['follower_count'] > A['follower_count']:
            # correct answer
            new_element = hl_data.data.pop(random.randint(0,len(hl_data.data) - 1))
            return 1 + play_game(B, new_element)
        else:
            print("Sorry, that's wrong.")
            return 0

if __name__ == "__main__":
    
    # Pop two random list elements to seed the game
    A = hl_data.data.pop(random.randint(0,len(hl_data.data) - 1))
    B = hl_data.data.pop(random.randint(0,len(hl_data.data) - 1))
    final_score = play_game(A, B)
    print(f"Final score: {final_score}")