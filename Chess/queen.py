from Game.constants import CHESS_WHITE

class Queen:
    Points = 9

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        if self.color == CHESS_WHITE:
            self.role = 'Q'
        else:
            self.role = 'q'

    def getValidMoves(self, pieces):
        # Returns list of valid moves.
        validMoves = []
        return validMoves
