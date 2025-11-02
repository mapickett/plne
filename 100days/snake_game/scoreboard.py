from turtle import Turtle

ALIGN = "center"
FONT = ('Courier New', 12, 'bold')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.penup()
        self.hideturtle()
        self.setposition(0,280)
        self.pencolor("white")
        self.update_scoreboard()
   
    def update_scoreboard(self):
        self.setposition(0,280)
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=True, align=ALIGN, font=FONT)

    def increment(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.setposition(0,0)
        self.write("GAME OVER", move=True, align=ALIGN, font=FONT)