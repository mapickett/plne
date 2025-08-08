import random
import my_module

random_number = random.randint(1,10)

print(random_number)
print(my_module.my_favorite_number)

print(random.random() * 10)
print(f"{random.uniform(1,10)}")
print(f"{random.uniform(1,10):.0f}")

flip = random.randint(0,1)
print(f"Heads is 0, Tails is 1")
result = "Tails!" if flip else "Heads!"
print(f"Your flip is {flip}, {result}")

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
pick = random.randint(0, len(friends) - 1)
print(f"{friends[pick]} pays the bill!")
print(f"{random.choice(friends)} pays the bill!")

bids ={
    'harry': 10,
    'Joe': 20,
    'Marry': 30
}

print(max(bids, key=bids.get))

def use_docs():
    """This is a doc string"""
    return

use_docs()

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    'multiply': lambda x, y: x * y
}
result_multiply = operations['multiply'](5, 3)
n1 = 1
n2 = 2
op1 = '+'
result = operations[op1](n1, n2)

# choice_map = {
#     "report": print_report,
#     "off": turn_off,
#     "espresso": lambda: brew_beverage("espresso"),
#     "latte": lambda: brew_beverage("latte"),
#     "cappucino": lambda: brew_beverage("cappucino")
# }
# choice_map[choice]()

def is_prime(num):
    for _ in range(2,num):
        if num % _ == 0:
            return False
    return True

print(is_prime(7))

# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight, my_screen.canvwidth)
# my_screen.exitonclick()

import prettytable

table = prettytable.PrettyTable()
table.header_style = "cap"
table.add_column("name", ['bill', 'bob', 'ted'])
table.add_column("type", ['cowboy', 'farmer', 'alcoholic'])
print(table)

class User:

    def __init__(self, user_id, username, hair_color='brown'):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        self.hair_color = hair_color

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User('001', 'angela')
user_2 = User('002', 'jack')
user_1.follow(user_2)


