from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.x_dist = 10
        self.y_dist = 10
        self.move_speed = 0.1
    
    def move(self):
        self.left(45)
        self.goto(self.xcor() + self.x_dist, self.ycor() + self.y_dist)

    def bounce_y(self):
        self.y_dist *= -1
    
    def bounce_x(self):
        self.x_dist *= -1
        self.move_speed *= 0.9

    def reset_postion(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1

