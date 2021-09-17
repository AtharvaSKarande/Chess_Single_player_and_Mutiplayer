import pygame.display

from Chess import get_row_col
from Game.values.colors import *
from Game.values.dimens import *
from Game.values.assets import *


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
        self.selectedPiece = None
        self.moveLoc = {}
        self.takesLoc = {}
        self.castleLoc = {}
        self.promotionMove = None

    def drawDisplay(self):
        # self.win.fill(MenuColor)
        self.drawTitle()
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
                    pygame.draw.rect(self.win, CHESS_BLACK, ((x, y), (SquareDimen, SquareDimen)))
                else:
                    pygame.draw.rect(self.win, CHESS_WHITE, ((x, y), (SquareDimen, SquareDimen)))

        self.drawUIMoves()
        self.drawPieces()
        self.drawCoordinates()
        self.drawPromotion()
        self.drawPlayers()
        self.drawEvalBar()
        self.drawFEN()
        pygame.display.update()

    def drawTitle(self):
        self.win.blit(title, (TitleStartX, TitleStartY))

    def drawMenu(self):
        pygame.draw.rect(self.win, MenuColor, ((MenuStartX, MenuStartY), (MenuLenX, MenuLenY)))

        txtX = (TitleStartX + TitleLenX) // 2
        txtY = MenuStartY + padding * 3 + MenuBtnHeight

        pygame.draw.rect(self.win, CHESS_WHITE, (((txtX - padding - ArrowBtnLenX, MenuStartY + padding),
                                                  (ArrowBtnLenX, ArrowBtnLenY))), 0, 8)
        pygame.draw.rect(self.win, CHESS_WHITE, ((txtX + padding, MenuStartY + padding),
                                                 (ArrowBtnLenX, ArrowBtnLenY)), 0, 8)
        # self.win.blit(BackArrow, (txtX - padding - ArrowBtnLenX, MenuStartY + padding))
        # self.win.blit(ForwardArrow, (txtX + padding, MenuStartY + padding))

        # Buttons
        for buttonTxt in ['Save Game', 'Settings', 'Continue with bot', 'Request Draw', 'Resign']:
            pygame.draw.rect(self.win, MenuBtnColor, ((MenuStartX + MenuBtnLeftPad, txtY), (MenuBtnWidth, MenuBtnHeight)
                                                      ), 0, 8)
            self.drawText(buttonTxt, MenuBtnFntSize, txtX, txtY, MenuBtnTextColor, centre='X')
            txtY += MenuBtnHeight + padding

        # Placing Quit button at end.
        txtY = MenuStartY + MenuLenY - padding - MenuBtnHeight
        pygame.draw.rect(self.win, MenuBtnColor, ((MenuBtnLeftPad, txtY), (MenuBtnWidth, MenuBtnHeight)), 0, 8)
        self.drawText('Quit', MenuBtnFntSize, txtX, txtY, MenuBtnTextColor, centre='X')
        txtY += MenuBtnHeight + padding

    def drawCoordinates(self):
        font = pygame.font.Font(gameFontBold, 20)
        for number in coordinates.keys():
            if number % 2:
                clr = CHESS_WHITE
            else:
                clr = CHESS_BLACK

            text = font.render(str(coordinates[number]), True, clr)
            textRect = text.get_rect()
            X = BoardStartX + padding + number * SquareDimen - textRect.center[0] - 3
            Y = 8 * SquareDimen + padding - textRect.center[1]
            textRect.center = (X, Y)
            self.win.blit(text, textRect)

            text = font.render(str(number), True, clr)
            textRect = text.get_rect()
            X = BoardStartX + padding + textRect.center[0] + 3
            Y = padding + (8 - number) * SquareDimen + textRect.center[1]
            textRect.center = (X, Y)
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
        checkY = BoardStartY + padding + abs(7 - row) * SquareDimen
        X = checkX + (SquareDimen - PieceDimen) // 2
        Y = checkY + (SquareDimen - PieceDimen) // 2

        if piece == 'TAKE':
            pygame.draw.circle(self.win, TakeColor, (checkX + SquareDimen // 2, checkY + SquareDimen // 2),
                               SquareDimen // 2, 7)
        elif piece == 'MOVE':
            pygame.draw.circle(self.win, MoveColor, (checkX + SquareDimen // 2, checkY + SquareDimen // 2),
                               10, 10)
        elif piece == 'CASTLE':
            pygame.draw.circle(self.win, CastleColor, (checkX + SquareDimen // 2, checkY + SquareDimen // 2),
                               10, 10)
        elif piece == 'SELECT':
            pygame.draw.rect(self.win, SelectColor, ((checkX, checkY), (SquareDimen, SquareDimen)))

        elif piece == 'P':
            self.win.blit(WHITE_PAWN, (X, Y))
        elif piece == 'p':
            self.win.blit(BLACK_PAWN, (X, Y))

        elif piece == 'K':
            if self.chessBoard.is_check() and self.chessBoard.turn:
                pygame.draw.rect(self.win, CheckColor, ((checkX, checkY), (SquareDimen, SquareDimen)))
            self.win.blit(WHITE_KING, (X, Y))
        elif piece == 'k':
            if self.chessBoard.is_check() and not self.chessBoard.turn:
                pygame.draw.rect(self.win, CheckColor, ((checkX, checkY), (SquareDimen, SquareDimen)))
            self.win.blit(BLACK_KING, (X, Y))

        elif piece == 'Q':
            self.win.blit(WHITE_QUEEN, (X, Y))
        elif piece == 'q':
            self.win.blit(BLACK_QUEEN, (X, Y))

        elif piece == 'B':
            self.win.blit(WHITE_BISHOP, (X, Y))
        elif piece == 'b':
            self.win.blit(BLACK_BISHOP, (X, Y))

        elif piece == 'R':
            self.win.blit(WHITE_ROOK, (X, Y))
        elif piece == 'r':
            self.win.blit(BLACK_ROOK, (X, Y))

        elif piece == 'N':
            self.win.blit(WHITE_KNIGHT, (X, Y))
        elif piece == 'n':
            self.win.blit(BLACK_KNIGHT, (X, Y))

    def drawPlayer1(self, turn=False):
        pygame.draw.rect(self.win, CHESS_WHITE, (P1StartX, P1StartY, P1LenX, P1LenY))
        pad = int(P1LenY * 0.1)
        if turn:
            pygame.draw.rect(self.win, turnColor, (P1StartX, P1StartY, P1LenY, P1LenY))
        pygame.draw.rect(self.win, CHESS_BLACK, (P1StartX + pad, P1StartY + pad, SquareDimen, SquareDimen))
        self.win.blit(WHITE_KING, (P1StartX + pad, P1StartY + pad))

        self.drawText(self.chessBoard.p1Name, 36, P1StartX + 3 * pad + SquareDimen, P1StartY + (padding+SquareDimen)//2,
                      CHESS_BLACK, centre='Y', font=gameFontBold)
        # self.drawText(self.chessBoard.p1Rating, 22, P1StartX + 3 * pad + SquareDimen, P1StartY + 4 * pad,
        # RatingFC, RatingBC, font=gameFontBold)

    def drawPlayer2(self, turn=False):
        pygame.draw.rect(self.win, CHESS_BLACK, (P2StartX, P2StartY, P2LenX, P2LenY))
        pad = int(P2LenY * 0.1)
        if turn:
            pygame.draw.rect(self.win, turnColor, (P2StartX, P2StartY, P1LenY, P1LenY))
        pygame.draw.rect(self.win, CHESS_WHITE, (P2StartX + pad, P2StartY + pad, SquareDimen, SquareDimen))
        self.win.blit(BLACK_KING, (P2StartX + pad, P2StartY + pad))

        self.drawText(self.chessBoard.p2Name, 36, P2StartX + 3 * pad + SquareDimen, P2StartY + (padding+SquareDimen)//2,
                      CHESS_WHITE, centre='Y', font=gameFontBold)
        # self.drawText(self.chessBoard.p2Rating, 22, P2StartX + 3 * pad + SquareDimen, P2StartY + 4 * pad,
        # RatingFC, RatingBC, font=gameFontBold)

    def drawPlayers(self):
        if self.chessBoard.turn:
            self.drawPlayer1(turn=True)
            self.drawPlayer2()
        else:
            self.drawPlayer1()
            self.drawPlayer2(turn=True)

    def isGameEnd(self):
        if self.chessBoard.is_checkmate():
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
        elif self.chessBoard.win_by_resignation():
            if self.chessBoard.winner == CHESS_BLACK:
                print("Black won by resignation.")
            else:
                print("White won by resignation.")
        elif self.chessBoard.draw_accepted:
            print("Draw Accepted.")
        else:
            return False
        return True

    def drawEvalBar(self):
        """
        pygame.draw.rect(self.win, BorderColor, (EvalBarStartX, EvalBarStartY, EvalBarLenX, EvalBarLenY))
        # here, 18 = fontSize, 9 = fontSize/2, 27 = fontSize*(3/2)
        yLen = HEIGHT - 2 * padding - 18 - 18 - 9 - 9
        self.drawText(self.chessBoard.p2_adv, 18, EvalBarStartX + EvalBarLenX // 2,
                      padding + 9, CHESS_BLACK, centre=True)
        self.drawText(self.chessBoard.p1_adv, 18, EvalBarStartX + EvalBarLenX // 2,
                      HEIGHT - padding - 9, CHESS_WHITE, centre=True)

        DarkLen = int(yLen * (100 - self.chessBoard.win_percent) / 100)
        pygame.draw.rect(self.win, CHESS_BLACK, (EvalBarStartX + padding, padding + 27, EvalBarWidth, DarkLen))
        pygame.draw.rect(self.win, CHESS_WHITE,
                         (EvalBarStartX + padding, padding + 27 + DarkLen, EvalBarWidth, yLen - DarkLen))"""
        pass

    def drawFEN(self):
        pygame.draw.rect(self.win, (100, 100, 100), (FENStartX, FENStartY, FENLenX, FENLenY))
        pass

    def menuClick(self, pos):
        row, col = pos
        if MenuStartX < row < MenuStartX + MenuLenX and MenuStartY < col < MenuStartY + MenuLenY:
            centre = MenuStartX + MenuLenX // 2

            # Backward and forward move
            if 0 < col - MenuStartY - padding < ArrowBtnLenY:
                if centre - padding - ArrowBtnLenX < row < centre - padding:
                    self.clearUIMoves()
                    success = self.chessBoard.move_back()
                    if not success:
                        print("Error")
                    self.updateBoard()

                elif 0 < row - centre - padding < ArrowBtnLenX:
                    self.clearUIMoves()
                    success = self.chessBoard.move()
                    if not success:
                        print("Error")
                    self.updateBoard()

            Y = MenuStartY + padding * 3 + MenuBtnHeight
            if 0 < row - MenuStartX - MenuBtnLeftPad < MenuBtnWidth:
                if MenuStartY + MenuLenY - padding - MenuBtnHeight < col < MenuStartY + MenuLenY - padding:
                    print("Game quit.")
                    pygame.quit()
                    return 0

                if Y < col < Y + MenuBtnHeight:
                    self.chessBoard.save_board()
                    print('Game saved.')
                    return 1
                Y += padding + MenuBtnHeight

                if Y < col < Y + MenuBtnHeight:
                    print("Settings")
                    return 1
                Y += padding + MenuBtnHeight

                if Y < col < Y + MenuBtnHeight:
                    print("Continue with bot")
                    return 1
                Y += padding + MenuBtnHeight

                if Y < col < Y + MenuBtnHeight:
                    # print("Request draw")
                    self.chessBoard.request_draw()
                    return 1
                Y += padding + MenuBtnHeight

                if Y < col < Y + MenuBtnHeight:
                    # print("Resign")
                    self.chessBoard.resign()
                    return 1

    def click(self, pos):
        pos = getRowColFromPos(pos)
        if pos != (-1, -1):
            col, row = pos
            row = abs(7 - row)
        else:
            self.clearUIMoves()
            return

        if self.promotionMove:
            if row == 3 and col == 3:
                self.chessBoard.move(self.promotionMove + 'B')
            if row == 3 and col == 4:
                self.chessBoard.move(self.promotionMove + 'N')
            if row == 4 and col == 3:
                self.chessBoard.move(self.promotionMove + 'Q')
            if row == 4 and col == 4:
                self.chessBoard.move(self.promotionMove + 'R')
            self.clearUIMoves()
            self.updateBoard()
            return

        clickedPiece = self.chessBoard.pieces[row][col]
        my_color = CHESS_BLACK
        if self.chessBoard.turn:
            my_color = CHESS_WHITE

        # Clicked piece is empty.
        if clickedPiece == '.':
            if self.selectedPiece:
                if (row, col) in self.moveLoc.keys():
                    if '=' in self.moveLoc[(row, col)]:
                        self.promotionMove = self.moveLoc[(row, col)][:-1]
                        self.updateBoard()
                        return
                    else:
                        self.chessBoard.move(self.moveLoc[(row, col)])
                elif (row, col) in self.takesLoc.keys():  # En-passant is take with clicked position = empty.
                    self.chessBoard.move(self.takesLoc[(row, col)])
                elif (row, col) in self.castleLoc.keys():
                    self.chessBoard.move(self.castleLoc[(row, col)])
            else:
                return

        # Clicked piece is of opponent's color.
        elif clickedPiece.color != my_color:
            if self.selectedPiece:
                if (row, col) in self.takesLoc.keys():
                    if '=' in self.takesLoc[(row, col)]:
                        self.promotionMove = self.takesLoc[(row, col)][:-1]
                        self.updateBoard()
                        return
                    else:
                        self.chessBoard.move(self.takesLoc[(row, col)])
            else:
                return

        # Clicked piece is of turn's color.
        else:
            if not self.selectedPiece:
                self.setUIMoves(clickedPiece)
            if clickedPiece != self.selectedPiece:
                self.clearUIMoves()
                self.setUIMoves(clickedPiece)
            self.updateBoard()
            return
        self.clearUIMoves()
        self.updateBoard()

    def setUIMoves(self, clickedPiece):
        self.selectedPiece = clickedPiece
        board = self.chessBoard
        if self.selectedPiece.role in ['P', 'p'] and (board.moveCount - 1) in board.en_passants.keys():
            moves = clickedPiece.getValidMoves(board, board.en_passants[board.moveCount - 1])
        else:
            moves = clickedPiece.getValidMoves(board)
        for mv in moves:
            if 'x' in mv:
                self.takesLoc[get_row_col(mv[5:7])] = mv
            elif '-' in mv:
                row = 7
                if board.turn:
                    row = 0
                if mv == 'O-O':
                    self.castleLoc[(row, 6)] = mv
                if mv == 'O-O-O':
                    self.castleLoc[(row, 2)] = mv
            else:
                self.moveLoc[get_row_col(mv[5:7])] = mv

    def drawUIMoves(self):
        for move in self.moveLoc.keys():
            self.showPiece('MOVE', move[0], move[1])
        for take in self.takesLoc.keys():
            self.showPiece('TAKE', take[0], take[1])
        for castle in self.castleLoc.keys():
            self.showPiece('CASTLE', castle[0], castle[1])
        if self.selectedPiece:
            self.showPiece('SELECT', self.selectedPiece.row, self.selectedPiece.col)

    def clearUIMoves(self):
        self.promotionMove = None
        self.selectedPiece = None
        self.moveLoc.clear()
        self.takesLoc.clear()
        self.castleLoc.clear()

    def drawPromotion(self):
        if self.promotionMove:
            X = BoardStartX + padding + 3 * SquareDimen
            Y = BoardStartY + padding + 3 * SquareDimen
            pygame.draw.rect(self.win, promotionColor, (X, Y, 2 * SquareDimen, 2 * SquareDimen))
            if self.chessBoard.turn:
                self.showPiece('Q', 4, 3)
                self.showPiece('R', 4, 4)
                self.showPiece('B', 3, 3)
                self.showPiece('N', 3, 4)
            else:
                self.showPiece('q', 4, 3)
                self.showPiece('r', 4, 4)
                self.showPiece('b', 3, 3)
                self.showPiece('n', 3, 4)

    def drawText(self, text, size, txtX, txtY, color, colorBg=None, font=gameFont, centre=False):
        Txt = pygame.font.Font(font, size).render(text, True, color, colorBg)
        nameRect = Txt.get_rect()
        if centre in [False, 'X', 'Y']:
            if centre == 'Y':
                txtX += nameRect.center[0]
            elif centre == 'X':
                txtY += nameRect.center[1]
            else:
                txtX += nameRect.center[0]
                txtY += nameRect.center[1]
        nameRect.center = (txtX, txtY)
        self.win.blit(Txt, nameRect)
