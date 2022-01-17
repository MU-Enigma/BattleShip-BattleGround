from BoardEngine.BoardEngineCore import Game

class Battleship(Game):

    __board0 = []  # __ makes board a private var.
    __board1 = []

    players = []
    permissibleMoves = []  # Keeps track of which move the player gets to currently play, used for special moves)

    def __init__(self):
        super().__init__()

        self.boardSize = [10, 10]
        self.gamePieces = [
            [1, 4]  # of format breadth, length
        ]  # List of pieces each player gets

    def initialize(self):
        assert len(self.players) == 2
        locations1 = self.players[0].placePieces()
        locations2 = self.players[1].placePieces()
        self.__board0 = self.generateBoard(locations1)
        self.__board1 = self.generateBoard(locations2)

    def update(self):
        baseInformation = []  # Common information given to every player at the start of each round in the game.
        for player in self.players:
            playerMove = player.makeMove(baseInformation)
            legal = self.verify(playerMove)

            if legal:
                """make list of if statements to react to playerMove.
                
                ex:
                
                if playerMove[0] == 4: (4 stands for get restricted information special move)
                    info = self.getRestrictedInfo(playerMove[1])
                    player.giftCache = info
                .
                .
                .     
                """

            #Also update self.GameInfo accordingly
            winval = self.checkWin()
            if winval != -1:
                #update game info accordinly to reflect winner, should probably put this if statement at the top.
                return True #Returns 1 for game completed
            return False #Returns 0 for game incomplete

    # ----------------------------------------------------------------------------------------------------------------
    # The functions above are overrided, below are game specific functions

    def verify(self, move):
        """

        :param move: standard player move
        :return: return False for illegal move, returns True for legal move
        """

    def checkWin(self):
        winner = 0 #integer, can be -1 for no winner yet, 0 for player0

        return

    def generateBoard(self, locations):
        bsize = self.boardSize
        board = [[]]

        # Make sure to check if locations are legal.
        # generate variable 'board'

        # Should return matrix of stuff
        return self.generateSpecialRegions(board)

    def generateSpecialRegions(self, board):
        # Assumes that there is only 1 type of special region

        # Do stuff here

        return board

    # ----------------------------------------------------------------------------------------------------------------
    # Move specific funtions

    def strike(self, boardnum, x, y):
        """

        :param boardnum: which player's board
        :param x: x-coor
        :param y: y-coor
        """

    def getRestrictedInfo(self, infoRequest):
        Info = []

        # execute the infoRequest

        return Info