from Game.constants import CHESS_WHITE

class Knight:
    Points = 3

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        if self.color == CHESS_WHITE:
            self.role = 'N'
        else:
            self.role = 'n'

    def getValidMoves(self):
        # Returns list of valid moves.
        pass
