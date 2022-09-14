from turtle import Turtle


class Scoreboard(Turtle):

    score = 0

    def __init__(self) -> None:
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.setposition(0, 475)
        self.write_score()

    def write_score(self) -> None:
        """Writes score data to the screen."""
        self.clear()
        self.write(
            f"Score: {self.score}",
            False,
            align="center",
            font=("Courier", 20, "bold"),
        )

    def update_score(self) -> None:
        """Adds a point to the score and updates the score data on the screen."""
        self.score += 1
        self.write_score()

    def game_over(self) -> None:
        """Displays the \"Game Over\" message."""
        self.setposition(0, 0)
        self.write("GAME OVER!", False, align="center", font=("Courier", 20, "bold"))
        pass
