from BoardEngine.BoardEngineCore import Player

class myPlayer(Player):

    giftCache = None # Used for 'get restricted information special move'. Should be cleared by myPlayer at each move after using the gift.
    internalState = []

    def __init__(self):
        super().__init__()
        self.playerName = "myName"

    # Game specific functions below

    def placePieces(self, boardsize, pieces):
        location = [] # should be of format (x-coor, y-coor, orientation), must be a legal.
        for x in range(boardsize):
            for y in range(boardsize):
                pass

    def makeMove(self, gameInfo):
        """
        :param gameInfo:
        :return: (moveID, move)
        Since there are multiple possible moves i.e strike (normal move) and multiple other special moves. We return in this format.
        For a normal strike move, The ID is 0 and the move is of the form (x, y). Thus, in this case we would return
        (0, (x-coor, y-coor))
        """