from Game.constants import CHESS_WHITE

class Queen:
    def __init__(self, row, col, color):
        self.points = 9
        self.row = row
        self.col = col
        self.color = color

        if self.color == CHESS_WHITE:
            self.role = 'Q'
        else:
            self.role = 'q'

    def getValidMoves(self):
        # Returns list of valid moves.
        pass
