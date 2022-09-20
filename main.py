from turtle import _Screen, Screen
from snake import Snake
from food import Food
from scroreboard import Scoreboard
import time


def initialize_screen() -> _Screen:
    screen = Screen()
    screen.setup(width=1000, height=1000)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    return screen


def main() -> None:
    screen = initialize_screen()
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(key="Up", fun=snake.move_up)
    screen.onkey(key="Down", fun=snake.move_down)
    screen.onkey(key="Left", fun=snake.move_left)
    screen.onkey(key="Right", fun=snake.move_right)

    game_running = True
    while game_running:
        screen.update()
        time.sleep(0.1)

        snake.move()

        if snake.head_segment.distance(food) < 15:
            food.move()
            snake.extend()
            scoreboard.update_score()

        if (
            snake.head_segment.xcor() > 490
            or snake.head_segment.xcor() < -490
            or snake.head_segment.ycor() > 490
            or snake.head_segment.ycor() < -490
        ):
            scoreboard.reset()
            snake.reset()

        for segment in snake.segments[1:]:
            if snake.head_segment.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()

    # scoreboard.reset()
    screen.exitonclick()


if __name__ == "__main__":
    main()
