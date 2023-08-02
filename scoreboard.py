from turtle import Turtle

FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.speed("fastest")
        self.print_score()
    
    def update_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align = "center", font = FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = "center", font = FONT)

