from turtle import Turtle

ALIGNMENT = "center"
FONT = ( 'Arial', 11, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(x=0, y=280)

    def show_score(self):
        """" Shows the score """
        self.write(f'Score: {self.score}', align= ALIGNMENT, font= FONT)

    def game_end(self):
        """ Displays When the snake hits the wall """
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)

    def add_score(self):
        """"Adds to the Score"""
        self.clear()
        self.score += 1

