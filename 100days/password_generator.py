import random
import string

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
symbols = list(string.punctuation)
numbers = list(range(10))

prompt1 = "How many letters would you like in your password?[0-255]: "
prompt2 = "How many symbols would you like in your password?[0-255]: "
prompt3 = "How many numbers would you like in your password?[0-255]: "

def get_int(prompt):
    while True:
        choice = input(prompt)
        try:
            choice = int(choice)
            if choice in range(256):
                return choice
            else:
                print("Invalid choice") 
        except ValueError:
            print("Invalid choice")


print("Welcome to the Password Generator")
num_letters = get_int(prompt1)
num_symbols = get_int(prompt2)
num_numbers = get_int(prompt3)

password_list = list()
for _ in range(num_letters):
    password_list.append(random.choice(letters))
for _ in range(num_symbols):
    password_list.append(random.choice(symbols))
for _ in range(num_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password= ""
for c in password_list:
    password += str(c)
print(f'The password is: {password}')


