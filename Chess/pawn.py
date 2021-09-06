from Game.constants import CHESS_WHITE, coordinates

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
        # Need to design.
        validMoves = []
        if self.color == CHESS_WHITE:
            if self.row == 1:
                validMoves.append("P_"+coordinates[self.col+1]+str(self.row+1)+"_"+coordinates[self.col+1]+str(self.row+3))
        else:
            pass
        return validMoves
