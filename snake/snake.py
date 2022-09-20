from turtle import Turtle
from typing import TypedDict

# Types
COORDINATES = TypedDict(
    "COORDINATES",
    {
        "UP": int,
        "DOWN": int,
        "LEFT": int,
        "RIGHT": int,
    },
)

MOVE_DISTANCE = 20
MOVE_DIRECTIONS: COORDINATES = {
    "UP": 90,
    "DOWN": 270,
    "LEFT": 180,
    "RIGHT": 0,
}


class Snake:

    segments: list[Turtle] = []
    head_segment: Turtle

    def __init__(self) -> None:
        self.create()

    def create(self) -> None:
        for i in range(3):
            self.add_segment((i * -20, 0))

        self.head_segment = self.segments[0]

    def add_segment(self, position: tuple[int, int]) -> None:
        """Adds a segment to the snake"""
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.speed("fastest")
        segment.setposition(position)
        segment.speed(0)

        self.segments.append(segment)

    def extend(self) -> None:
        """Extends the snake (used for extending the snake during the game)."""
        self.add_segment(self.segments[-1].position())

    def reset(self) -> None:
        for segment in self.segments:
            segment.setposition(1000, 1000)

        self.segments.clear()
        self.create()

    def move(self) -> None:
        """Moves the snake forward one move."""
        segments = self.segments

        for idx in range(len(segments) - 1, 0, -1):
            x, y = segments[idx - 1].position()
            segments[idx].setposition(x, y)

        segments[0].forward(MOVE_DISTANCE)

    def move_up(self) -> None:
        """Points the snake's head upward."""
        if self.head_segment.heading() != MOVE_DIRECTIONS["DOWN"]:
            self.head_segment.setheading(MOVE_DIRECTIONS["UP"])

    def move_down(self) -> None:
        """Points the snake's head downward."""
        if self.head_segment.heading() != MOVE_DIRECTIONS["UP"]:
            self.head_segment.setheading(MOVE_DIRECTIONS["DOWN"])

    def move_right(self) -> None:
        """Points the snake's head to the right."""
        if self.head_segment.heading() != MOVE_DIRECTIONS["LEFT"]:
            self.head_segment.setheading(MOVE_DIRECTIONS["RIGHT"])

    def move_left(self) -> None:
        """Points the snake's head to the left."""
        if self.head_segment.heading() != MOVE_DIRECTIONS["RIGHT"]:
            self.head_segment.setheading(MOVE_DIRECTIONS["LEFT"])
