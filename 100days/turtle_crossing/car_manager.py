from turtle import Turtle
import random

CAR_COLORS = ["black", "brown", "red", "blue", "green", "yellow", "orange", "grey"]
STARTING_POSITIONS = [(288, -235), (288, -205), (288, -175), (288, -145), (288, -115),
                    (288, -85), (288, -55), (288, -25), (288, 5), (288, 35),
                    (288, 65), (288, 95), (288, 125), (288, 155), (288, 185),
                    (288, 215)]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car_Manager(Turtle):

    def __init__(self):
        self.cars = []
        self.movement_rate = STARTING_MOVE_DISTANCE

    def add_car(self):
        t = Turtle()
        t.shape("square")
        t.shapesize(stretch_len=2)
        t.color(random.choice(CAR_COLORS))
        t.penup()
        t.setpos(random.choice(STARTING_POSITIONS))
        t.setheading(180)
        self.cars.append(t)
    
    def move_cars(self):
        for car in self.cars:
            car.forward(self.movement_rate)

    def speed_up(self):
        self.movement_rate += MOVE_INCREMENT