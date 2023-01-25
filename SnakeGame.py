from Game import *
from snake_util import *
from players import *
import random
import os
import time

pause = 0

class SnakeGame(Game):
    def __init__(self, x, y, playerTyp, print_game):
        self.dimX = x
        self.dimY = y
        self.state = None
        self.print_game = print_game
        self.playerType = playerTyp
        self.player = None
        self.numberOfMoves = 100
        self.gameOver = False
        self.isReady = False

    def initGame(self, seed = 0):

        if self.playerType == PlayerType.human:
            self.player = Human()
        elif self.playerType == PlayerType.random_player:
            self.player = RandomPlayer()
        elif self.playerType == PlayerType.straight_to_apple:
            self.player = StraightToApple()
        if seed != 0:
            random.seed(seed)

        headX = random.randint(0, self.dimX - 1)
        headY = random.randint(0, self.dimY - 1)
        appleX = random.randint(0, self.dimX - 1)
        appleY = random.randint(0, self.dimY - 1)

        while((appleX == headX) and (appleY == headY)):
            appleX = random.randint(0, self.dimX - 1)
            appleY = random.randint(0, self.dimY - 1)
        self.state = SnakeGameState(SnakeField(appleX, appleY), [SnakeField(headX, headY)], 0)
        self.isReady = True

    def play(self):
        while(not self.gameOver):
            self.display()
            action = self.getAction()
            self.state = self.takeTurn(action)
            self.checkGameOver()
            if self.print_game:
                time.sleep(pause)
        return self.state.applesEaten

    def takeTurn(self, action):

        oldSnake = self.state.snake
        oldHead = oldSnake[0]
        newHead = SnakeField(oldHead.x, oldHead.y)

        if(action == SnakeAction.left):
             newHead.x = newHead.x - 1
        elif(action == SnakeAction.right):
             newHead.x = newHead.x + 1
        elif(action == SnakeAction.top):
             newHead.y = newHead.y - 1
        elif(action == SnakeAction.bottum):
             newHead.y = newHead.y + 1

        for part in oldSnake:
            if part.x == newHead.x and part.y == newHead.y:
                self.gameOver = True
        newSnake = [newHead]

        applePos = self.state.applePos
        applesEaten = self.state.applesEaten
        offset = 1

        if(newHead.x == applePos.x and newHead.y == applePos.y):
            foundNewApple = False
            applesEaten = applesEaten + 1
            while(not foundNewApple):
                foundNewApple = True
                appleX = random.randint(0, self.dimX - 1)
                appleY = random.randint(0, self.dimY - 1)
                for snakePart in oldSnake:
                    if(appleX == snakePart.x and appleY == snakePart.y):
                        foundNewApple = False
            applePos = SnakeField(appleX, appleY)
            self.numberOfMoves = 500
            offset = 0
        
        for i in range(len(oldSnake) - offset):
            newSnake.append(oldSnake[i])

        newState = SnakeGameState( applePos, newSnake, applesEaten)
        return newState


    def checkGameOver(self):
        if self.numberOfMoves == 0:
            self.gameOver = True
            return

        self.numberOfMoves -= 1
        head = self.state.snake[0]
        if(head.x < 0 or head.x > self.dimX - 1 or head.y < 0 or head.y > self.dimY - 1):
            self.gameOver = True
            return

        for snakePart in self.state.snake[1:]:
            if (head.x == snakePart.x and head.y == snakePart.y):
                self.gameOver = True
            return


    def display(self):

        if not self.print_game:
            return

        os.system("cls")
        board = [[" " for i in range(self.dimX)]for j in range(self.dimY)]
        board[self.state.applePos.y][self.state.applePos.x] = "\033[91mX\033[0m"
        board[self.state.snake[0].y][self.state.snake[0].x] = "\033[92mO\033[0m"

        for snakePart in self.state.snake[1:]:
            board[snakePart.y][snakePart.x] = "\033[93mO\033[0m"
        
        str = "----------------------\n"
        for i in range(self.dimY):
            str = str + "|"
            for j in range(self.dimX):
                str = str + board[i][j]
            str = str + "|\n"
        str = str + "----------------------"
        print(str)

    def getAction(self):
        action = self.player.getAction(self.state)
        return action


