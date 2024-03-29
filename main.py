from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


def endgame():
    """Ends the game"""
    global game_is_on
    game_is_on = False


def start_game():
    game()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(endgame, 'e')
screen.onkey(start_game, "s")

screen.update()

game_is_on = True


def game():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.2)
        snake.move()

        # detects collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.add_score()

        score.show_score()

        # detects collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            score.reset()
            snake.reset()

        # Detects the tail
        for snakes in snake.all_snake[1:]:
            if snake.head.distance(snakes) < 10:
                score.reset()
                snake.reset()


screen.exitonclick()
