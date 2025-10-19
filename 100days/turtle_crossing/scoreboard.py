from turtle import Turtle

STARTING_POSITION = (-280, 260)
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.player_level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(STARTING_POSITION)
        self.write(f"Level: {self.player_level}", align='left', font=FONT)

    def score(self):
        self.player_level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)


