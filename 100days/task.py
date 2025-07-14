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
