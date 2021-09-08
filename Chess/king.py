from Game.constants import CHESS_WHITE


class King:
    Points = 0

    def __init__(self, row, col, color):
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
