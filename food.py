from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.6, 0.6)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rad_x = random.randint(-240, 240)
        rad_y = random.randint(-240, 240)
        self.goto(rad_x, rad_y)