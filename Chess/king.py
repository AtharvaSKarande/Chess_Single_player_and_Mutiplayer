from Game.constants import CHESS_WHITE

class King:
    def __init__(self, row, col, color):
        self.points = 0
        self.row = row
        self.col = col
        self.color = color

        if self.color == CHESS_WHITE:
            self.role = 'K'
        else:
            self.role = 'k'

    def getValidMoves(self):
        # Returns list of valid moves.
        pass
