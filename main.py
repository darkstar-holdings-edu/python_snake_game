from turtle import _Screen, Screen
from snake import Snake
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

    screen.exitonclick()
    pass


if __name__ == "__main__":
    main()
