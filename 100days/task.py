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
    '/': divide
}
n1 = 1
n2 = 2
op1 = '+'
result = operations[op1](n1, n2)

def is_prime(num):
    for _ in range(2,num):
        if num % _ == 0:
            return False
    return True

print(is_prime(7))
