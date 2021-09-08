from Game.constants import CHESS_WHITE

class Bishop:
    Points = 3

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        if self.color == CHESS_WHITE:
            self.role = 'B'
        else:
            self.role = 'b'

    def getValidMoves(self):
        # Returns list of valid moves.
        pass
