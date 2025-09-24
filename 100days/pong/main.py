from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

if __name__ == "__main__":
    
    STARTING_POSITIONS = [(0,275), (0,175), (0,75),
                          (0,-25), (0,-125), (0,-225)]

    screen = Screen()

    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Let's Play Pong!")
    screen.tracer(0)

    for position in STARTING_POSITIONS:
        t = Turtle()
        t.pensize(5)
        t.hideturtle()
        t.color("white")
        t.penup()
        t.setpos(position)
        t.pendown()
        t.setheading(270)
        t.forward(50)
    
    player1 = Paddle("Player1")
    player2 = Paddle("Player2")
    ball = Ball()
    scoreboard = Scoreboard()   

    screen.listen()
    screen.onkey(player1.up, "w")
    screen.onkey(player1.down, "s")
    screen.onkey(player2.up, "Up")
    screen.onkey(player2.down, "Down")
    screen.onkey(ball.set_pause, "p")
    
    playing = True
    while playing:
        screen.update()
        time.sleep(.005)
        ball.move()
        if ball.paddle_miss():
            scoreboard.score(ball)
            ball.reset()
        elif ball.paddle_hit(player1, player2):
            ball.hit()
        elif ball.wall_collision():
            ball.bounce()

    screen.exitonclick()
