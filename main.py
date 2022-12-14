import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

scoreboard = Score()
snake = Snake()
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
food = Food()

game = True

snake.generate_snake()
while game:
    screen.update()
    time.sleep(snake.speed)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.ampliar_cobra()
        food.refresh()
        scoreboard.aumentar_pontuacao()
        snake.speed -= 0.002
    if snake.head.ycor() > 299 or snake.head.ycor() < - 299 or snake.head.xcor() > 299 or snake.head.xcor() < -299:
        scoreboard.reset()
        snake.reset()
        food.refresh()

    for parte in snake.turtles[1:]:
        if snake.head.distance(parte) < 10:
            scoreboard.reset()
            snake.reset()
            food.refresh()

screen.exitonclick()
