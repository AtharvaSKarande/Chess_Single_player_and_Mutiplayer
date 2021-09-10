from Game.constants import CHESS_WHITE
from .static import get_board_co_ord

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

    def getValidMoves(self, pieces, en_passant_col='-1'):
        validMoves = []
        direction = -1
        mv = 'P_' + get_board_co_ord(self.row, self.col) + '_'
        if self.color == CHESS_WHITE:
            direction = 1

        # If pawn is not moved, play 2 moves if possible
        if direction == 1 and self.row == 1 and pieces[self.row + 2][self.col] == '.':
            validMoves.append(mv + get_board_co_ord(self.row + 2, self.col))
        elif direction == -1 and self.row == 6 and pieces[self.row - 2][self.col] == '.':
            validMoves.append(mv + get_board_co_ord(self.row - 2, self.col))

        # En-passants
        if en_passant_col != '-1':
            if direction == 1 and self.row == 4 and abs(en_passant_col - self.col) == 1:
                validMoves.append(mv + get_board_co_ord(self.row + 1, en_passant_col) + 'xP')
            elif direction == -1 and self.row == 3 and abs(en_passant_col - self.col) == 1:
                validMoves.append(mv + get_board_co_ord(self.row - 1, en_passant_col) + 'xP')

        # Promotions
        if (direction == 1 and self.row == 6) or (direction == -1 and self.row == 1):
            if pieces[self.row + direction][self.col] == '.':
                nxtPlace = get_board_co_ord(self.row + direction, self.col)
                validMoves.append(mv + nxtPlace + '=Q')
                validMoves.append(mv + nxtPlace + '=R')
                validMoves.append(mv + nxtPlace + '=N')
                validMoves.append(mv + nxtPlace + '=B')
            if 0 <= self.col-1 <= 7 and pieces[self.row + direction][self.col-1] != '.':
                nxtPlace = get_board_co_ord(self.row + direction, self.col-1)
                takenPieceRole = pieces[self.row + direction][self.col-1].role.upper()
                validMoves.append(mv + nxtPlace + 'x' + takenPieceRole + '=Q')
                validMoves.append(mv + nxtPlace + 'x' + takenPieceRole + '=R')
                validMoves.append(mv + nxtPlace + 'x' + takenPieceRole + '=N')
                validMoves.append(mv + nxtPlace + 'x' + takenPieceRole + '=B')
            if 0 <= self.col+1 <= 7 and pieces[self.row + direction][self.col+1] != '.':
                nxtPlace = get_board_co_ord(self.row + direction, self.col+1)
                takenPieceRole = pieces[self.row + direction][self.col+1].role.upper()
                validMoves.append(mv + nxtPlace + 'x' + takenPieceRole + '=Q')
                validMoves.append(mv + nxtPlace + 'x' + takenPieceRole + '=R')
                validMoves.append(mv + nxtPlace + 'x' + takenPieceRole + '=N')
                validMoves.append(mv + nxtPlace + 'x' + takenPieceRole + '=B')

        # Pawn 1 move and takes.
        if (direction == 1 and self.row != 6) or (direction == -1 and self.row != 1):
            if pieces[self.row + direction][self.col] == '.':
                validMoves.append(mv + get_board_co_ord(self.row + direction, self.col))

            if 0 <= self.col-1 <= 7:
                pieceTk = pieces[self.row + direction][self.col - 1]
                if pieceTk != '.' and pieceTk.color != self.color:
                    nxtPlace = get_board_co_ord(self.row + direction, self.col-1)
                    takenPieceRole = pieceTk.role.upper()
                    validMoves.append(mv + nxtPlace + 'x' + takenPieceRole)

            if 0 <= self.col+1 <= 7:
                pieceTk = pieces[self.row + direction][self.col+1]
                if pieceTk != '.' and pieceTk.color != self.color:
                    nxtPlace = get_board_co_ord(self.row + direction, self.col+1)
                    takenPieceRole = pieceTk.role.upper()
                    validMoves.append(mv + nxtPlace + 'x' + takenPieceRole)
        return validMoves
