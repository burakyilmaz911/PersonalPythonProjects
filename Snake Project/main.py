from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
#
# def add_to_snake():
#     snake_tail = Turtle()
#     snake_tail.color("white")
#     snake_tail.shape("square")
#     snake_tail.pos()
#     snake_blocks.append(snake_tail)




screen.exitonclick()