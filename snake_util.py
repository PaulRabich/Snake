from Game import *

class SnakeAction(GameAction):
    left = 0
    right = 1
    bottum = 2
    top = 3

class SnakeField:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SnakeGameState(GameState):
    def __init__(self, applePos, snakePos, applesEaten):
        self.applePos = applePos
        self.snake = snakePos
        self.applesEaten = applesEaten