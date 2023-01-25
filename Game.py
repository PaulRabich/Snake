class GameState:
    pass

class GameAction:
    pass

class Game:

    def initGame(self):
        pass

    def takeTurn(self, state, action):
        pass

    def endGame(self):
        pass

    def display(self):
        pass

class PlayerType:
    human = 0
    bot = 1
    random_player = 2
    straight_to_apple = 3