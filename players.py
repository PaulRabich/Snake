import keyboard
import time
import random
from snake_util import *

class Player:

    def getAction(self, game_state):
        return 0

    
class Human(Player):
    def __init__(self):
        keyboard.on_release(lambda e: self.setLastKey(e))
        self.last_key = None

    def getAction(self, game_state):
        self.last_key = None
        while(self.last_key == None):
            time.sleep(0.1)
            keyTyped = self.last_key
            self.last_key = None
            if(keyTyped == None):
                continue
            if(keyTyped == 'w'):
                return SnakeAction.top
            elif(keyTyped == 's'):
                return SnakeAction.bottum
            elif(keyTyped == 'd'):
                return SnakeAction.right
            elif(keyTyped == 'a'):
                return SnakeAction.left

    def setLastKey(self, key):
        self.last_key = key.name

class RandomPlayer(Player):
    def getAction(self, game_state):
        moves = [SnakeAction.top, SnakeAction.bottum, SnakeAction.left, SnakeAction.right]
        return random.choice(moves)

class StraightToApple(Player):
    def getAction(self, game_state):
        applePos = game_state.applePos
        appleX = applePos.x
        appleY = applePos.y
        headPos = game_state.snake[0]
        headX = headPos.x
        headY = headPos.y
        xDif = headX - appleX
        yDif = headY - appleY
        if abs(xDif) > abs(yDif):
            if(xDif < 0): 
                return SnakeAction.right 
            else: 
                return SnakeAction.left
        else:
            if(yDif < 0): 
                return SnakeAction.bottum 
            else: 
                return SnakeAction.top 

    