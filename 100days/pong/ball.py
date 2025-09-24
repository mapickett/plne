from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")       
        self.color("white")
        self.reset()
        self.pause = False
        self.movement_rate = 1
    
    def reset(self):
        self.penup()
        self.setpos(0,0)
        self.setheading(random.randint(0,359))
        self.movement_rate = 1

    def move(self):
        if not self.pause:
            self.forward(self.movement_rate)

    def set_pause(self):
        if self.pause:
            self.pause = False
        else:
            self.pause = True

    def wall_collision(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            return True
        else:
            return False
        
    def paddle_miss(self):
        if self.xcor() > 380 or self.xcor() <= -380:
            return True
        else:
            return False

    def bounce(self):
        heading = self.heading()
        if 0 <= heading < 90:
            new_heading = 0 - heading
        elif heading == 90:
            new_heading = 85
        elif 90 < heading <= 180:
            new_heading = 180 + (180 - heading)
        elif 180 < heading < 270:
            new_heading = 180 - (heading - 180)
        elif heading == 270:
            new_heading = 275
        elif 270 < heading < 360:
            new_heading = 90 - (heading - 270)
        self.setheading(new_heading)


    def paddle_hit(self, player1, player2):
        xcor = self.xcor()
        ycor = self.ycor()
        paddle1 = player1.ycor()
        paddle2 = player2.ycor()
        if xcor <= -330:
            if  paddle1 - 50 <= ycor <= paddle1 + 50:
                return True
        if xcor >= 330:
            if  paddle2 - 50 <= ycor <= paddle2 + 50:
                return True
        return False

    def hit(self):
        heading = self.heading()
        if heading == 0:
            new_heading = 185
        elif 0 < heading < 90:
            new_heading = 90 + (90 - heading)
        elif 90 <= heading < 180:
            new_heading = 0 + (180 - heading)
        elif heading == 180:
            new_heading = 5
        elif 180 < heading < 270:
            new_heading = 0 - (heading - 180)
        elif 270 <= heading < 359:
            new_heading = 180 + (360 - heading)
        self.setheading(new_heading)
        for i in range(10):
            self.move()
        self.movement_rate += 1

    def bounce(self):
        heading = self.heading()
        if 0 <= heading < 90:
            new_heading = 0 - heading
        elif heading == 90:
            new_heading = -85
        elif 90 < heading <= 180:
            new_heading = 180 + (180 - heading)
        elif 180 < heading < 270:
            new_heading = 180 - (heading - 180)
        elif heading == 270:
            new_heading = 95
        elif 270 < heading < 360:
            new_heading = 90 - (heading - 270)
        self.setheading(new_heading)