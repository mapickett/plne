from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
STARTING_POSITIONS = {
    'Player1': (-350,0),
    'Player2': (350,0)
}

class Paddle(Turtle):

    def __init__ (self, player):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.penup()
        self.setpos(STARTING_POSITIONS[player])
        
    def up(self):
        if self.ycor() < 240:
            self.setheading(UP)
            self.forward(MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -240:
            self.setheading(DOWN)
            self.forward(MOVE_DISTANCE)
