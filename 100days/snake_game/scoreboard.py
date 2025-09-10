from turtle import Turtle

ALIGN = "center"
FONT = ('Courier New', 12, 'bold')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setposition(0,280)
        self.pencolor("white")
        self.update_scoreboard()
   
    def update_scoreboard(self):
        self.setposition(0,280)
        self.write(f"Score: {self.score}", move=True, align=ALIGN, font=FONT)

    def increment(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setposition(0,0)
        self.write("GAME OVER", move=True, align=ALIGN, font=FONT)