from Game.constants import CHESS_WHITE

class Pawn:
    def __init__(self, row, col, color):
        self.points = 1
        self.row = row
        self.col = col
        self.color = color

        if self.color == CHESS_WHITE:
            self.role = 'P'
        else:
            self.role = 'p'

    def getValidMoves(self):
        # Returns list of valid moves.
        pass
