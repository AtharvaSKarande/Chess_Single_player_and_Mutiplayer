from Game.constants import CHESS_WHITE

class Pawn:
    Points = 1

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        if self.color == CHESS_WHITE:
            self.role = 'P'
        else:
            self.role = 'p'

    def getValidMoves(self, en_passants):
        # Returns list of valid moves.
        pass
