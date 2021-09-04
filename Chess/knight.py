from Game.constants import CHESS_WHITE

class Knight:
    def __init__(self, row, col, color):
        self.points = 3
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
