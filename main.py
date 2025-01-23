from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score_board import Score

screen = Screen()
screen.setup(width= 500, height= 500)
screen.bgcolor("Black")
screen.title("🐍 Snake Game")
screen.tracer(0)

segments = []
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend_segment()
        food.refresh()
        
    if snake.head.xcor() > 250 or snake.head.xcor() < -250 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
        score.game_over()
        game_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()