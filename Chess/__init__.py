from Game.constants import CHESS_WHITE, CHESS_BLACK, coordinates, letters
from .bishop import Bishop
from .pawn import Pawn
from .king import King
from .rook import Rook
from .queen import Queen
from .knight import Knight


class chessBoard:
    def __init__(self):

        # 7     r n b q k b n r
        # 6     p p p p p p p p
        # 5     . . . . . . . .
        # 4     . . . . . . . .
        # 3     . . . . . . . .
        # 2     . . . . . . . .
        # 1     P P P P P P P P
        # 0     R N B Q K B N R
        #
        #       0 1 2 3 4 5 6 7
        self.w_king = King(0, 4, CHESS_WHITE)
        self.b_king = King(7, 4, CHESS_BLACK)

        self.pieces = [
            [Rook(0, 0, CHESS_WHITE), Knight(0, 1, CHESS_WHITE), Bishop(0, 2, CHESS_WHITE), Queen(0, 3, CHESS_WHITE),
             self.w_king, Bishop(0, 5, CHESS_WHITE), Knight(0, 6, CHESS_WHITE), Rook(0, 7, CHESS_WHITE)],

            [Pawn(1, 0, CHESS_WHITE), Pawn(1, 1, CHESS_WHITE), Pawn(1, 2, CHESS_WHITE), Pawn(1, 3, CHESS_WHITE),
             Pawn(1, 4, CHESS_WHITE), Pawn(1, 5, CHESS_WHITE), Pawn(1, 6, CHESS_WHITE), Pawn(1, 7, CHESS_WHITE)],

            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],

            [Pawn(6, 0, CHESS_BLACK), Pawn(6, 1, CHESS_BLACK), Pawn(6, 2, CHESS_BLACK), Pawn(6, 3, CHESS_BLACK),
             Pawn(6, 4, CHESS_BLACK), Pawn(6, 5, CHESS_BLACK), Pawn(6, 6, CHESS_BLACK), Pawn(6, 7, CHESS_BLACK)],

            [Rook(7, 0, CHESS_BLACK), Knight(7, 1, CHESS_BLACK), Bishop(7, 2, CHESS_BLACK), Queen(7, 3, CHESS_BLACK),
             self.b_king, Bishop(7, 5, CHESS_BLACK), Knight(7, 6, CHESS_BLACK), Rook(7, 7, CHESS_BLACK)]
        ]
        self.turn = True

        # white pieces
        self.white_pawns = 8
        self.white_dark_bishops = 1
        self.white_light_bishops = 1
        self.white_knights = 2
        self.white_rooks = 2
        self.white_queens = 1
        self.white_king = 1
        # black pieces
        self.black_pawns = 8
        self.black_dark_bishops = 1
        self.black_light_bishops = 1
        self.black_knights = 2
        self.black_rooks = 2
        self.black_queens = 1
        self.black_king = 1

        self.en_passants = []

        # Winning percentage of white
        self.win_percent = 50

        # Castling rights
        self.castle_rights = ['K', 'Q', 'k', 'q']
        # Problem may arise for castling during back move.
        self.moveList = []
        self.winner = None

        self.p1_adv = "0.00"
        self.p2_adv = "-0.00"

    def print_board(self):
        for i in self.pieces:
            for j in i:
                if j != '.':
                    print(j.role, end=" ")
                else:
                    print('.', end=' ')
            print()

    def move(self, move):
        # 'P_e4_e5' - Pawn from e4 to e5.
        # 'P_e5_f6' - Pawn from e5 to f6 (En-Passant).
        # 'O-O' - Short castle.
        # 'O-O-O' - Long Castle.
        # 'R_a4_a8xB' - Rook from a4 to a8 takes Bishop.
        # 'P_e7_e8=Q' - Pawn form e7 to e8 promoted to Queen.
        # 'P_e7_f8xQ=N' - Pawn from e7 to f8 takes Queen promoted to Knight.

        if self.turn:
            color = CHESS_WHITE
        else:
            color = CHESS_BLACK
        if move not in self.get_all_valid_moves(color):
            print("Invalid Move")
            return

        self.moveList.append(move)

        if move == 'O-O':
            if self.turn:
                self.pieces[0][4], self.pieces[0][6] = self.pieces[0][6], self.pieces[0][4]
                self.pieces[0][6].col = 6
                self.pieces[0][5], self.pieces[0][7] = self.pieces[0][7], self.pieces[0][5]
                self.pieces[0][5].col = 5

                try:
                    self.castle_rights.remove('K')
                    self.castle_rights.remove('Q')
                except ValueError:
                    pass
            else:
                self.pieces[7][4], self.pieces[7][6] = self.pieces[7][6], self.pieces[7][4]
                self.pieces[7][6].col = 6
                self.pieces[7][5], self.pieces[7][7] = self.pieces[7][7], self.pieces[7][5]
                self.pieces[7][5].col = 5

                try:
                    self.castle_rights.remove('k')
                    self.castle_rights.remove('q')
                except ValueError:
                    pass

        elif move == 'O-O-O':
            if self.turn:
                self.pieces[0][2], self.pieces[0][4] = self.pieces[0][4], self.pieces[0][2]
                self.pieces[0][2].col = 2
                self.pieces[0][0], self.pieces[0][3] = self.pieces[0][3], self.pieces[0][0]
                self.pieces[0][3].col = 3

                try:
                    self.castle_rights.remove('Q')
                    self.castle_rights.remove('K')
                except ValueError:
                    pass

            else:
                self.pieces[7][2], self.pieces[7][4] = self.pieces[7][4], self.pieces[7][2]
                self.pieces[7][2].col = 2
                self.pieces[7][0], self.pieces[7][3] = self.pieces[7][3], self.pieces[7][0]
                self.pieces[7][3].col = 3

                try:
                    self.castle_rights.remove('q')
                    self.castle_rights.remove('k')
                except ValueError:
                    pass

        elif move[-2] == '=':
            newPos = (move[6] - 1, letters[move[5]] - 1)
            oldPos = (move[3] - 1, letters[move[2]] - 1)
            self.pieces[oldPos[0]][oldPos[1]] = '.'

            if self.turn:
                self.white_pawns -= 1

                if 'x' in move:
                    capturedPiece = move[1 + move.find('x')]
                    if capturedPiece == 'B':
                        if newPos[1] % 2:
                            self.black_dark_bishops -= 1
                        else:
                            self.black_light_bishops -= 1
                    elif capturedPiece == 'N':
                        self.black_knights -= 1
                    elif capturedPiece == 'Q':
                        self.black_queens -= 1
                    elif capturedPiece == 'R':
                        self.black_rooks -= 1
                    # Pawns can not reside on 8th or 1st rank.

                if move[-1] == 'B':
                    if newPos[1] % 2:
                        self.white_dark_bishops += 1
                    else:
                        self.white_light_bishops += 1
                    self.pieces[newPos[0]][newPos[1]] = Bishop(newPos[0], newPos[1], CHESS_WHITE)
                elif move[-1] == 'N':
                    self.white_knights += 1
                    self.pieces[newPos[0]][newPos[1]] = Knight(newPos[0], newPos[1], CHESS_WHITE)
                elif move[-1] == 'Q':
                    self.white_queens += 1
                    self.pieces[newPos[0]][newPos[1]] = Queen(newPos[0], newPos[1], CHESS_WHITE)
                elif move[-1] == 'R':
                    self.white_rooks += 1
                    self.pieces[newPos[0]][newPos[1]] = Rook(newPos[0], newPos[1], CHESS_WHITE)

            else:
                self.black_pawns -= 1

                if 'x' in move:
                    capturedPiece = move[1 + move.find('x')]
                    if capturedPiece == 'B':
                        if newPos[1] % 2:
                            self.white_dark_bishops -= 1
                        else:
                            self.white_light_bishops -= 1
                    elif capturedPiece == 'N':
                        self.white_knights -= 1
                    elif capturedPiece == 'Q':
                        self.white_queens -= 1
                    elif capturedPiece == 'R':
                        self.white_rooks -= 1
                    # Pawns can not reside on 8th or 1st rank.

                if move[-1] == 'B':
                    if newPos[1] % 2:
                        self.black_light_bishops += 1
                    else:
                        self.black_dark_bishops += 1
                    self.pieces[newPos[0]][newPos[1]] = Bishop(newPos[0], newPos[1], CHESS_BLACK)
                elif move[-1] == 'N':
                    self.black_knights += 1
                    self.pieces[newPos[0]][newPos[1]] = Knight(newPos[0], newPos[1], CHESS_BLACK)
                elif move[-1] == 'Q':
                    self.black_queens += 1
                    self.pieces[newPos[0]][newPos[1]] = Queen(newPos[0], newPos[1], CHESS_BLACK)
                elif move[-1] == 'R':
                    self.black_rooks += 1
                    self.pieces[newPos[0]][newPos[1]] = Rook(newPos[0], newPos[1], CHESS_BLACK)

        else:
            newPos = (move[6] - 1, letters[move[5]] - 1)
            oldPos = (move[3] - 1, letters[move[2]] - 1)

            self.pieces[newPos[0]][newPos[1]], self.pieces[oldPos[0]][oldPos[1]] = \
                self.pieces[oldPos[0]][oldPos[1]], '.'

            if self.turn:
                if 'x' in move:
                    capturedPiece = move[1 + move.find('x')]
                    if capturedPiece == 'B':
                        if (newPos[0] + newPos[1]) % 2:
                            self.black_light_bishops -= 1
                        else:
                            self.black_dark_bishops -= 1
                    elif capturedPiece == 'N':
                        self.black_knights -= 1
                    elif capturedPiece == 'Q':
                        self.black_queens -= 1
                    elif capturedPiece == 'R':
                        self.black_rooks -= 1
                    elif capturedPiece == 'P':
                        self.black_pawns -= 1
                        # if En-passant
                        if move[0] == 'P' and oldPos[0] == 4 and newPos[0] == 5 and abs(oldPos[1] - newPos[1]) == 1:
                            self.pieces[oldPos[0]][newPos[1]] = '.'
            else:
                if 'x' in move:
                    capturedPiece = move[1 + move.find('x')]
                    if capturedPiece == 'B':
                        if (newPos[0] + newPos[1]) % 2:
                            self.white_light_bishops -= 1
                        else:
                            self.white_dark_bishops -= 1
                    elif capturedPiece == 'N':
                        self.white_knights -= 1
                    elif capturedPiece == 'Q':
                        self.white_queens -= 1
                    elif capturedPiece == 'R':
                        self.white_rooks -= 1
                    elif capturedPiece == 'P':
                        self.white_pawns -= 1
                        # if En-passant
                        if move[0] == 'P' and oldPos[0] == 3 and newPos[0] == 2 and abs(oldPos[1] - newPos[1]) == 1:
                            self.pieces[oldPos[0]][newPos[1]] = '.'

        self.en_passants.clear()
        self.moveList.append(move)
        self.evaluate_advantage()

    def is_check(self, row=None, col=None):
        pass

    def is_checkmate(self):
        pass

    def draw_by_insufficient_material(self):
        white_bishops = self.white_dark_bishops + self.white_light_bishops
        black_bishops = self.black_dark_bishops + self.black_light_bishops

        if self.white_queens == 0 and self.black_queens == 0 and self.white_rooks == 0 and self.black_rooks == 0 \
                and self.white_pawns == 0 and self.black_pawns == 0:
            # check for two kings
            if white_bishops == 0 and black_bishops == 0 and self.white_knights == 0 and self.black_knights == 0:
                return True
            # check for two kings and white knight
            elif white_bishops == 0 and black_bishops == 0 and self.white_knights == 1 and self.black_knights == 0:
                return True
            # check for two kings and black knight
            elif white_bishops == 0 and black_bishops == 0 and self.white_knights == 0 and self.black_knights == 1:
                return True
            # check for two kings and white bishop
            elif white_bishops == 1 and black_bishops == 0 and self.white_knights == 0 and self.black_knights == 0:
                return True
            # check for two kings and black bishop
            elif white_bishops == 0 and black_bishops == 1 and self.white_knights == 0 and self.black_knights == 0:
                return True
            # check for two kings and two bishops(same colored)
            elif self.white_dark_bishops == 1 and self.black_dark_bishops == 1 and self.white_knights == 0 \
                    and self.black_knights == 0:
                return True
            # check for two kings and two bishops(same colored)
            elif self.white_light_bishops == 1 and self.black_light_bishops == 1 and self.white_knights == 0 \
                    and self.black_knights == 0:
                return True
            else:
                return False

    def draw_by_threefold_repetition(self):
        pass

    def get_all_valid_moves(self, color=None):
        if not color:
            if self.turn:
                color = CHESS_WHITE
            else:
                color = CHESS_BLACK

        validMoves = list()
        for row in self.pieces:
            for piece in row:
                if piece != '.' and piece.color == color:
                    validMoves.append(piece.getValidMoves())
        return validMoves

    def evaluate_advantage(self):
        pass

    def draw_by_stalemate(self):
        if not self.get_all_valid_moves():
            return True
        return False

    def resign(self):
        if self.turn:
            self.winner = CHESS_BLACK
        else:
            self.winner = CHESS_WHITE
