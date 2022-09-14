from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.setposition(self.get_random_position())

    def get_random_position(self) -> tuple[int, int]:
        """Gets a random x, y coordinate."""
        position = tuple([random.randint(-280, 280) for _ in range(2)])
        return (position[0], position[1])

    def move(self) -> None:
        """Moves the food to a random position on the screen."""
        self.setposition(self.get_random_position())
