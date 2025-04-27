# String Slicing

movie = 'The Godfather'
print(movie[0:2])

# string_variable[start:stop]
print(movie[:4]) # exclusive - includes poisiton 0, excludes position 4
print(movie[4:]) # inclusive - includes position 4
print(movie[:4] + movie[4:])

# step value
print(movie[4::2])

print(movie[::])
print(movie[::-1])