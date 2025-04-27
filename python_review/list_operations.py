# LIST OPERATIONS

l1 = [3, 4]
print(l1, id(l1))
l1 = l1 + [5,6]
print(l1, id(l1))
l1 += [7,8]
print(l1, id(l1))
l1.extend([11, 12])
print(l1, id(l1))

# append adds a single element to the end
# extend adds all items from an iterable
# l1.append(20)
# l1.extend([20])

l2 = list('abc')
l3 = l2 * 3
print(l3)

print('#' * 10 + ' LIST SLICING ' + '#' * 10)
numbers = [1, 2, 3, 4, 5]
nums = numbers[1:4]
print(f'nums: {nums}')
print(f'numbers: {numbers}')
print(f'numbers: {numbers[:3]}')
print(f'numbers: {numbers[2:]}')
print(f'numbers: {numbers[::-1]}')

numbers[0:1] = ['a', 'b']
print(f'numbers: {numbers}')

numbers[0:2] = ['a', 'b', 'c', 'd']
print(f'numbers: {numbers}')

numbers[0:4] = [1]
print(f'numbers: {numbers}')

print('#' * 10 + ' LIST ITERATION ' + '#' * 10)
ip_list = ['192.168.0.1', '192.168.0.2', '192.168.0.3']
for ip in ip_list:
    print(f'Connecting to {ip} ...')

