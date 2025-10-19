from turtle import Turtle,Screen
from player import Player
from car_manager import Car_Manager
from scoreboard import Scoreboard
import time

SOLID_LINES = [(300, 230), (300, -250)]
DASHED_LINES = [(288, -220), (288, -190), (288, -160), (288, -130), (288, -100),
                (288, -70), (288, -40), (288, -10), (288, 20), (288, 50),
                (288, 80), (288, 110), (288, 140), (288, 170), (288, 200),
                (288, 230)]
CAR_INTERVAL = 10

if __name__ == "__main__":

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Let's Play Turtle Crossing")
    screen.tracer(0)
    
    for position in SOLID_LINES:
        t = Turtle()
        t.pensize(1)
        t.hideturtle()
        t.color("black")
        t.penup()
        t.setpos(position)
        t.pendown()
        t.setheading(180)
        t.forward(600)

    for position in DASHED_LINES:
        t = Turtle()
        t.pensize(1)
        t.hideturtle()
        t.color("black")
        t.penup()
        t.setpos(position)
        t.setheading(180)
        for _ in range(12):
            t.pendown()
            t.forward(25)
            t.penup()
            t.forward(25)

    player = Player()
    scoreboard = Scoreboard()
    car_manager = Car_Manager()

    screen.listen()
    screen.onkey(player.move, "Up")

    playing = True
    loop_counter = 0
    while playing:

        # Generate Cars
        if loop_counter % CAR_INTERVAL == 0:
            car_manager.add_car()
        if loop_counter == CAR_INTERVAL:
            loop_counter = 0
        else:
            loop_counter +=1
        
        # Move Cars
        car_manager.move_cars()

        # Check for successful crossing
        if player.crossed_road():
            scoreboard.score()
            player.reset()
            car_manager.speed_up()

        # Check for hit by car
        if player.hit_by_car(car_manager):
            scoreboard.game_over()
            playing = False

        screen.update()
        time.sleep(0.1)

    screen.exitonclick()