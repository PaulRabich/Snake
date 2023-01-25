from SnakeGame import *
from Game import *



snake = SnakeGame(20, 10, PlayerType.straight_to_apple, True)
snake.initGame(seed = 1)
snake.play()