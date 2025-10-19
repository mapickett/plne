from turtle import Turtle

STARTING_POSITION = (0, -265)
MOVE_DISTANCE = 10
FINISH_LINE = 255

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.reset()

    def reset(self):
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(90)
        self.movement_rate = MOVE_DISTANCE

    def move(self):
        self.forward(self.movement_rate)

    def crossed_road(self):
        if self.ycor() >= FINISH_LINE:
            return True
        return False
    
    def hit_by_car(self, car_manager):
        xcor = self.xcor()
        ycor = self.ycor()
        for car in car_manager.cars:
            # if (car.xcor() - 25 <= xcor <= car.xcor() + 25 and
            #     car.ycor() - 10 <= ycor <= car.ycor() + 10):
            if self.distance(car) < 20:
              return True
        return False