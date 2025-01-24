from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 220)
        self.score_calc()      

    def score_calc(self):
        self.clear()
        self.write(f"Score: {self.score}", align = "center", font = ("Arial", 12, "bold"))
        
    def increase_score(self):
        self.score += 1
        self.score_calc()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = "center", font = ("Arial", 14, "bold"))