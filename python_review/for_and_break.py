# For, else and break statements

print('#' * 10)

for number in range(10):
    print(number)
    if number == 5:
        break

print('#' * 10)

# exit() will stop the entire script

for letter in 'Python':
    if letter == 'o':
        print('Letter is o and breaking out of loop')
        break
    print(letter)

print('#' * 10)

for n in range(1, 20):
    if n % 13 == 0:
        print('There is a number divisible by 13 in the range. Breaking out ...')
        break
else: # belongs to the for loop
    print('There\'s no number divisible by 13 in the range.')

print('#' * 10)

for letter in 'Python':
    print(letter)
    for n in range(3):
      if n == 1:
          break
      print(n)
