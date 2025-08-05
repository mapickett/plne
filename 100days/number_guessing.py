import art
import random










if __name__ == "__main__":

    print(art.number_guess)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    my_number = random.randint(1,100)
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty in ['easy', 'hard']:
            break
    if difficulty == 'easy':
        chances = 10
    else:
        chances = 5
    found = False
    while chances and not found:
        print(f"You have {chances} attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        try:
            guess = int(guess)
            if guess == my_number:
                found = True
            elif guess < my_number:
                print("Too low.\nGuess again.")
            else:
                print("Too high.\nGuess again.")
        except:
            print("You must guess a number between 1 and 100.")
        chances -= 1
    if found:
        print(f"You got it! Than answer was {my_number}. ")
    else:
        print("You've run out of guesses.")