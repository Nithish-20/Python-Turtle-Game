from turtle import Turtle
    
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write("SCORE", align = "center", font = ("Courier", 24, "bold"))
        self.goto(-120, 240)
        self.write(self.l_score, align = "center", font = ("Courier", 24, "bold"))
        self.goto(120, 240)
        self.write(self.r_score, align = "center", font = ("Courier", 24, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_score()
    
    def r_point(self):
        self.r_score += 1
        self.update_score()