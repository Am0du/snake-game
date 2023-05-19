from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 11, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode='r') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(x=0, y=280)

    def show_score(self):
        """" Shows the score """
        self.clear()
        self.write(f'Score: {self.score}  High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.score}")

        self.score = 0

    def add_score(self):
        """"Adds to the Score"""
        self.score += 1
        self.show_score()
