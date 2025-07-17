BANNER = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/         '''

HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
    +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']

from random_word import RandomWords
r = RandomWords()

# Return a single random word
answer = r.get_random_word().lower()

hidden_answer = '_' * len(answer)
guesses = []
lives = 6
winner = False

def get_letter():
    while True:
        choice = input("Guess a letter: ")
        if choice.isalpha() and len(choice) == 1:
            if choice in guesses:
                print(f'You already guessed {choice}')
            else:
                guesses.append(choice)
                return choice.lower()
        else:
            print("Invalid choice")

print(BANNER)
while lives and not winner:
    print(HANGMANPICS[lives])
    print(f'You have {lives} lives remaining.')
    print(f'Your guesses: {guesses}')
    print(f'Word to guess: {hidden_answer}')
    
    # Get Guess
    guess = get_letter()

    #Update hidden_answer
    for x in range(len(answer)):
        if guess == answer[x]:
            hidden_answer = hidden_answer[:x] + answer[x] + hidden_answer[x+1:]

    if guess not in answer:
        lives -= 1
        print(f'Sadly, "{guess}" is not in the word')
    else:
        print(f'You found the letter {guess}!')
    if '_' not in hidden_answer:
        winner = True
    print("*" * 50)

print(f'The word was {answer}')
if winner:
    print("You win!")
else:
    print("You lose!")
    print(HANGMANPICS[lives])