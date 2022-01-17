"""



"""


class Player:

    def __init__(self):
        self.playerName = 'playerName'


class Game:

    GameConfig = {
        "name": "game",
        "render": False
    }  # Can be changed during initialization of child Game.

    __GameInfo = [] #Stores information related to the game ex: Move history, time taken, etc...

    def __init__(self):
        pass

    def initialize(self):
        pass


    def update(self):
        pass


    def run(self, players):
        self.players = players
        while not self.update():
            pass
        return self.__GameInfo


    # Below functions are redundant currently but will add functionality later:

    def draw(self):
        pass

    def runMoves(self):
        pass

    def broadcast(self):
        pass
