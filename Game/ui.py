import pygame.display
from Game.constants import *

def getRowColFromPos(pos):
    row, col = pos
    if BoardStartX + padding < row < BoardStartX + padding + 8 * SquareDimen:
        if padding < col < HEIGHT - padding - 1:
            return min((row - BoardStartX - padding) // SquareDimen, 7), min((col - padding) // SquareDimen, 7)
    return -1, -1

class UI:
    def __init__(self, win, chessBoard):
        self.win = win
        self.chessBoard = chessBoard

    def drawDisplay(self):
        self.win.fill(MenuColor)
        self.drawMenu()
        self.updateBoard()
        pygame.display.update()

    def updateBoard(self):
        pygame.draw.rect(self.win, BorderColor, (BoardStartX, BoardStartY, BoardLen, BoardLen))
        for i in range(8):
            for j in range(8):
                x = BoardStartX + padding + j * SquareDimen
                y = BoardStartY + padding + i * SquareDimen
                if (i + j) % 2:
                    pygame.draw.rect(self.win, BoardDark, ((x, y), (SquareDimen, SquareDimen)))
                else:
                    pygame.draw.rect(self.win, BoardLight, ((x, y), (SquareDimen, SquareDimen)))

        self.drawPieces()
        self.drawCoordinates()
        self.drawTurn()
        self.drawEvalBar()
        self.drawPreviousMoves()
        pygame.display.update()

    def drawMenu(self):
        pass

    def drawCoordinates(self):
        font = pygame.font.Font(gameFontBold, 18)
        for number in coordinates.keys():
            if number % 2:
                clr = BoardLight
            else:
                clr = BoardDark

            text = font.render(str(coordinates[number]), True, clr)
            textRect = text.get_rect()
            textRect.center = (BoardStartX + padding * 0.5 + number * SquareDimen, padding * 0.4 + 8 * SquareDimen)
            self.win.blit(text, textRect)

            text = font.render(str(number), True, clr)
            textRect = text.get_rect()
            textRect.center = (BoardStartX + padding * 1.6, padding * 1.8 + (8 - number) * SquareDimen)
            self.win.blit(text, textRect)

    def drawPieces(self):
        FEN = self.chessBoard.pieces
        for row in FEN:
            for piece in row:
                if piece != '.':
                    self.showPiece(piece.role, piece.row, piece.col)
        return

    def showPiece(self, piece, row, col):
        checkX = BoardStartX + padding + col * SquareDimen
        checkY = BoardStartY + padding + abs(7-row) * SquareDimen
        X = checkX + (SquareDimen - PieceDimen) // 2
        Y = checkY + (SquareDimen - PieceDimen) // 2

        if piece == 'P':
            self.win.blit(WHITE_PAWN, (X, Y))
        elif piece == 'p':
            self.win.blit(BLACK_PAWN, (X, Y))

        if piece == 'K':
            self.win.blit(WHITE_KING, (X, Y))
        elif piece == 'k':
            self.win.blit(BLACK_KING, (X, Y))

        '''if piece == 'K':
            if self.board.is_check() and self.board.turn:
                pygame.draw.rect(self.win, CheckColor, ((checkX, checkY), (SquareDimen, SquareDimen)))
            self.win.blit(WHITE_KING, (X, Y))
        elif piece == 'k':
            if self.board.is_check() and not self.board.turn:
                pygame.draw.rect(self.win, CheckColor, ((checkX, checkY), (SquareDimen, SquareDimen)))
            self.win.blit(BLACK_KING, (X, Y))'''

        if piece == 'Q':
            self.win.blit(WHITE_QUEEN, (X, Y))
        elif piece == 'q':
            self.win.blit(BLACK_QUEEN, (X, Y))

        if piece == 'B':
            self.win.blit(WHITE_BISHOP, (X, Y))
        elif piece == 'b':
            self.win.blit(BLACK_BISHOP, (X, Y))

        if piece == 'R':
            self.win.blit(WHITE_ROOK, (X, Y))
        elif piece == 'r':
            self.win.blit(BLACK_ROOK, (X, Y))

        if piece == 'N':
            self.win.blit(WHITE_KNIGHT, (X, Y))
        elif piece == 'n':
            self.win.blit(BLACK_KNIGHT, (X, Y))

    def drawPlayer1(self, turn=False):
        pygame.draw.rect(self.win, BoardLight, (P1StartX, P1StartY, P1LenX, P1LenY))
        pad = int(P1LenY * 0.1)
        if turn:
            pygame.draw.rect(self.win, turnColor, (P1StartX, P1StartY, P1LenY, P1LenY))
        pygame.draw.rect(self.win, BoardDark, (P1StartX + pad, P1StartY + pad, SquareDimen, SquareDimen))
        self.win.blit(WHITE_PAWN, (P1StartX + pad, P1StartY + pad))

        self.drawText(P1Name, 24, P1StartX + 3 * pad + SquareDimen, P1StartY + pad, BoardDark)
        self.drawText(P1Rating, 22, P1StartX + 3 * pad + SquareDimen, P1StartY + 4 * pad,
                      RatingFC, RatingBC, font=gameFontBold)

    def drawPlayer2(self, turn=False):
        pygame.draw.rect(self.win, BoardDark, (P2StartX, P2StartY, P2LenX, P2LenY))
        pad = int(P2LenY * 0.1)
        if turn:
            pygame.draw.rect(self.win, turnColor, (P2StartX, P2StartY, P1LenY, P1LenY))
        pygame.draw.rect(self.win, BoardLight, (P2StartX + pad, P2StartY + pad, SquareDimen, SquareDimen))
        self.win.blit(BLACK_PAWN, (P2StartX + pad, P2StartY + pad))

        self.drawText(P2Name, 24, P2StartX + 3 * pad + SquareDimen, P2StartY + pad, BoardLight)
        self.drawText(P2Rating, 22, P2StartX + 3 * pad + SquareDimen, P2StartY + 4 * pad,
                      RatingFC, RatingBC, font=gameFontBold)

    def drawTurn(self):
        if self.chessBoard.turn:
            self.drawPlayer1(turn=True)
            self.drawPlayer2()
        else:
            self.drawPlayer1()
            self.drawPlayer2(turn=True)

    def isGameEnd(self):
        if self.chessBoard.is_check() and not self.chessBoard.is_checkmate():
            if self.chessBoard.turn:
                print("White checked")
            else:
                print("Black checked")
            return False

        elif self.chessBoard.is_checkmate():
            if self.chessBoard.turn:
                print("Checkmate : Black Won.")
            else:
                print("Checkmate : White Won.")

        elif self.chessBoard.draw_by_threefold_repetition():
            print("Draw by three fold Repetition.")
        elif self.chessBoard.draw_by_insufficient_material():
            print("Draw by insufficient material.")
        elif self.chessBoard.draw_by_stalemate():
            print("Draw by stalemate.")
        else:
            return False
        return True

    def drawEvalBar(self):
        pygame.draw.rect(self.win, BorderColor, (EvalBarStartX, EvalBarStartY, EvalBarLenX, EvalBarLenY))
        # here, 18 = fontSize, 9 = fontSize/2, 27 = fontSize*(3/2)
        yLen = HEIGHT - 2 * padding - 18 - 18 - 9 - 9
        self.drawText(self.chessBoard.p1_adv, 18, EvalBarStartX + EvalBarLenX // 2,
                      padding + 9, BoardDark, centre=True)
        self.drawText(self.chessBoard.p2_adv, 18, EvalBarStartX + EvalBarLenX // 2,
                      HEIGHT - padding - 9, BoardLight, centre=True)

        DarkLen = int(yLen * (100 - self.chessBoard.win_percent) / 100)
        pygame.draw.rect(self.win, BoardDark, (EvalBarStartX + padding, padding + 27, EvalBarWidth, DarkLen))
        pygame.draw.rect(self.win, BoardLight,
                         (EvalBarStartX + padding, padding + 27 + DarkLen, EvalBarWidth, yLen - DarkLen))

    def drawPreviousMoves(self):
        # pygame.draw.rect(self.win, PreviousMoveColor, (PreviousMoveStartX, PreviousMoveStartY,
        # PreviousMoveLenX, PreviousMoveLenY))
        pass

    def click(self, pos):
        pos = getRowColFromPos(pos)
        if pos != (-1, -1):
            row, col = pos
            col = abs(7-pos[1])
            print(col,row)

    def drawText(self, text, size, txtX, txtY, color, colorBg=None, font=gameFont, centre=False):
        Txt = pygame.font.Font(font, size).render(text, True, color, colorBg)
        nameRect = Txt.get_rect()
        if not centre:
            txtX += nameRect.center[0]
            txtY += nameRect.center[1]
        nameRect.center = (txtX, txtY)
        self.win.blit(Txt, nameRect)
