from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()  # init superclass
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 10 by 10 circle
        self.color('red')
        self.speed('fastest')
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)
