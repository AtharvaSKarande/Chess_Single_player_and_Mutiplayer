from Game.constants import CHESS_WHITE

class Rook:
    Points = 5

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        if self.color == CHESS_WHITE:
            self.role = 'R'
        else:
            self.role = 'r'

    def getValidMoves(self, pieces):
        # Returns list of valid moves.
        validMoves = []
        return validMoves
