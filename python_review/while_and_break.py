# While and break

from random import randint

my_number = randint(1,10)

while True:
    guess = int(input('Guess my number [1-10]:'))
    if guess == my_number:
        print('You won!')
        break
    print(f'{guess} is not my number!')

# a prime number is a number > 1 and divisible only by 1 and itself.
a = int(input('Enter Max Prime Value: '))
while a > 1: # satisfy definition of > 1
    b = a // 2 # Start testing for divisors at half a. Anything larger is 1.xxx
    while b > 1: # test for every number from .5a down to 2
        if a % b == 0: # if a mod b is 0 then a is not prime
            break
        b -= 1 # decrement b
    else:
        print(f'{a} is prime')
    a -= 1
