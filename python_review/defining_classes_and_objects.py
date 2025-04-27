# OOP: DEFINING CLASSES AND OBJECTS

class Robot:
    """This class implements a Robot."""
    population = 0
    def __init__(self, name, year): # dunder init; 'self' is a convention
        self.name = name
        self.year = year
        Robot.population += 1

    def __del__(self):
        print('Robot destroyed')
        Robot.population -= 1

    def setEnergy(self, energy):
        self.energy = energy

r1 = Robot(name='R1', year=2025)
r2 = Robot(name='R2D2', year=1977)

print(r1.__doc__) # dunder doc

print(r1.name, r1.year)

print(r1.__dict__) # internally sored as dict, can see with dunder dict

r1.setEnergy(500)
print(r1.energy)
print(getattr(r1, 'energy'))

print(getattr(r1, 'brand', 'N/A')) # support default value; avoids exception

# Class attributes defined at class level

print(f'Robots alive: {Robot.population}')

# dunder (double underscores) magic or special methods
# +  is short for __add__()
# a + b is the same as a.__add__(b)
# each operation has a magic method; automatically invoked 

class Brobot:
    """This class implements a Robot."""
    population = 0
    def __init__(self, name, price): # dunder init; 'self' is a convention
        self.name = name
        self.price = price
        Brobot.population += 1

    def __del__(self):
        print('Brobot destroyed')
        Brobot.population -= 1

    def __str__(self): # overloaded str operator
        my_str = f'My name is {self.name} and my price is {self.price}.'
        return my_str
    
    def __add__(self, other): # overloaded add operator
        price = self.price + other.price
        return price

b1 = Brobot(name='Marvin', price=150)
b2 = Brobot(name='Gil', price=45)

print(b1)   # overloaded str operator

print(b1 + b2) # overloaded add operator
