from turtle import Turtle
from scoreboard import Scoreboard
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake(Scoreboard):

    def __init__(self):
        super().__init__()
        self.all_snake = []
        self.x_cord = 0
        self.length = 3
        self.create_snake()
        self.head = self.all_snake[0]

    def create_snake(self):
        """this creates the snake body and saves it into the all_snake list"""
        for x in START_POSITION:
            self.add_snake(x)

    def add_snake(self, x):
        new_snake = Turtle('square')
        new_snake.penup()
        new_snake.color('white')
        new_snake.goto(x)
        self.all_snake.append(new_snake)

    def extend(self):
        self.add_snake(self.all_snake[-1].position())

    def move(self):
        """this starts  the for loop by taking the length of all_snake list minus 1 = 2, then takes a step -1:
        (2-1 = 1), and ends the loop when the position value changes to 0"""

        for position in range(len(self.all_snake) - 1, 0, -1):
            new_x = self.all_snake[position - 1].xcor()
            new_y = self.all_snake[position - 1].ycor()
            self.all_snake[position].goto(new_x, new_y)

        self.all_snake[0].forward(MOVE_DISTANCE)

    def reset(self):
        for snake in self.all_snake:
            snake.goto(1000, 1000)

        self.all_snake.clear()
        self.create_snake()
        self.head = self.all_snake[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.all_snake[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.all_snake[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.all_snake[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.all_snake[0].setheading(LEFT)


