# OOP DEMO: THE TURTLE

from turtle import Turtle, Screen
my_screen = Screen()
donatello = Turtle()
print(my_screen.canvwidth)
donatello.shape('turtle')
donatello.color('purple')
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.home()

raphael = Turtle()
raphael.shape('turtle')
raphael.color('red')
raphael.penup()
raphael.goto(-150, 200)
raphael.pendown()
raphael.pencolor('blue')

x = 10
while x <= 50:
    raphael.circle(x)
    donatello.circle(x+5)
    x += 10

my_screen.exitonclick()

# Abstraction - hides complexity from the user
# Encapsulation - binding attributes and methods as a single unit. 
#     Also known as data hiding.