from Game.constants import CHESS_WHITE

class Rook:
    def __init__(self, row, col, color):
        self.points = 5
        self.row = row
        self.col = col
        self.color = color

        if self.color == CHESS_WHITE:
            self.role = 'R'
        else:
            self.role = 'r'

    def getValidMoves(self):
        # Returns list of valid moves.
        pass
