# Converting lists to strings

# split() and join() - string methods

s1 = 'I am learning python programming'
l1 = s1.split() # uses whitespace by default
l2 = s1.split('p')
print(l1)
print(l2)

ip_list = ['192.168.0.1', '192.168.0.2', '192.168.0.3']
ip_str = ', '.join(ip_list)
print(ip_str)
