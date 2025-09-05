import turtle
import textwrap
import random

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

if __name__ == "__main__":

    s = turtle.Screen()
    s.setup(width=500, height=310)
    prompt = """
        Which turtle will win the race?
        Pick a color ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]: '
    """
    user_pick = s.textinput(title="Make Your Pick!", prompt=textwrap.dedent(prompt))
    colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
    racers = []

    for i in range(7):
        racer = turtle.Turtle(shape="turtle")
        racer.penup()
        racer.color(colors[i])
        racer.setpos(x=-230, y=-90 + 30*i)
        racers.append(racer)
    
    winner = []
    while not winner:
        for racer in racers:
            stride = random.randint(0,10)
            racer.forward(stride)
            if racer.xcor() >= 225:
                winner.append(racer.pencolor())

    print(f'You chose { user_pick }')
    if len(winner) > 1:
        print(f"There was a tie! The winners are { winner }")
    else:
        print(f"The winner is { winner[0] }")
    if user_pick in winner:
        print("Congratulations!!! You picked the Winner!")
    else:
        print("You lose. You did not pick the winner")

    s.exitonclick()
