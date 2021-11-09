import os
import pickle
from re import sub as re_sub
import time
from pygame import mixer
import pygame.display

from Chess.static import get_row_col
from ListView import ListView
from fruit import Fruit
from Game.utils import Theme, Language, FontSizes
from .values.colors import CHESS_WHITE, CHESS_BLACK
from .values.dimens import *
from .values.assets import *
from Game.utils import AlertDialog


def getBoardRowColFromPos(pos):
    row, col = pos
    if BoardStartX + padding < row < BoardStartX + padding + 8 * SquareDimen:
        if padding < col < HEIGHT - padding - 1:
            return min((row - BoardStartX - padding) // SquareDimen, 7), min((col - padding) // SquareDimen, 7)
    return -1, -1


class UI:
    def __init__(self, win, chessBoard, vsAI, aiColor, gameTheme, gameLang, volume=50, p1Name=None, p2Name=None):

        self.running = True
        self.preferences = (win, chessBoard, vsAI, aiColor, gameTheme, gameLang, volume, p1Name, p2Name)

        self.mixer = mixer
        self.mixer.init()
        self.mixer.music.load("assets/chessmove.wav")

        self.win = win
        self.chessBoard = chessBoard
        self.theme = Theme(gameTheme)
        self.txt = Language(gameLang)
        self.sizes = FontSizes(gameLang)
        self.selectedPiece = None
        self.moveLoc = {}
        self.takesLoc = {}
        self.castleLoc = {}
        self.promotionMove = None
        self.dialog = False

        self.gameVolume = volume
        self.vsAI = vsAI
        self.aiColor = aiColor
        self.aiMove = None

        self.aiStarted = None
        self.aiTurn = None
        if aiColor == CHESS_WHITE:
            self.aiTurn = True
        elif aiColor == CHESS_BLACK:
            self.aiTurn = False

        self.analysis = False

        self.p1Name = p1Name
        self.p2Name = p2Name

        if gameLang == 'HINDI':
            self.p1Name = self.txt.p1Name
            self.p2Name = self.txt.p2Name

        if vsAI and aiColor == CHESS_WHITE:
            self.p1Name = self.txt.p1Name
            self.p2Name = self.p1Name

        if not p1Name:
            self.p1Name = self.txt.p1Name
        if not p2Name:
            self.p2Name = self.txt.p2Name

        self.fruit = Fruit(self.chessBoard.moveList, self.theme.borderCLR, 60, FENLenX - 40, 2, 2, 5)
        self.listview = ListView(FENStartX + 20, FENStartY + 50, FENLenX - 40, HEIGHT - FENStartY - 100,
                                 self.fruit, self.theme.darkCLR, self.theme.lightCLR, 5, self.theme.borderCLR, 3, win)

    def drawDisplay(self):
        # self.win.fill(MenuColor)
        self.updateBoard()
        pygame.display.update()

    def updateBoard(self):
        self.drawTitle()
        self.drawMenu()
        pygame.draw.rect(self.win, self.theme.borderCLR, (BoardStartX, BoardStartY, BoardLenX, BoardLenY))
        for i in range(8):
            for j in range(8):
                x = BoardStartX + padding + j * SquareDimen
                y = BoardStartY + padding + i * SquareDimen
                if (i + j) % 2:
                    pygame.draw.rect(self.win, self.theme.darkCLR, ((x, y), (SquareDimen, SquareDimen)))
                else:
                    pygame.draw.rect(self.win, self.theme.lightCLR, ((x, y), (SquareDimen, SquareDimen)))

        self.mixer.music.set_volume(self.gameVolume / 100)
        self.mixer.music.play()
        self.drawUIMoves()
        self.drawPieces()
        self.drawCoordinates()
        self.drawPromotion()
        self.drawPlayers()
        self.drawEvalBar()
        self.drawInformation()
        self.drawFEN()
        self.isGameEnd()
        pygame.display.update()

    def drawTitle(self):
        pygame.draw.rect(self.win, self.theme.lightCLR, ((TitleStartX, TitleStartY), (TitleLenX, TitleLenY)))
        self.win.blit(title, (TitleStartX, TitleStartY))

    def drawMenu(self):
        pygame.draw.rect(self.win, self.theme.menuCLR, ((MenuStartX, MenuStartY), (MenuLenX, MenuLenY)))

        txtX = (TitleStartX + TitleLenX) // 2
        txtY = MenuStartY + btnPadding * 3 + MenuBtnHeight

        if self.chessBoard.moveList:
            pygame.draw.rect(self.win, self.theme.lightCLR, (
                (txtX - btnPadding - ArrowBtnLenX, MenuStartY + btnPadding), (ArrowBtnLenX, ArrowBtnLenY)), 0, 8)
            self.win.blit(BackArrow, (txtX - btnPadding - ArrowBtnLenX, MenuStartY + btnPadding))

        if self.chessBoard.poppedMoveList:
            pygame.draw.rect(self.win, self.theme.lightCLR, ((txtX + btnPadding, MenuStartY + btnPadding),
                                                             (ArrowBtnLenX, ArrowBtnLenY)), 0, 8)

            self.win.blit(ForwardArrow, (txtX + btnPadding, MenuStartY + btnPadding))

        # Buttons
        if not self.analysis:
            buttonList = [self.txt.new_game, self.txt.save_game, self.txt.settings]
            if self.vsAI:
                buttonList += [self.txt.continue_with_friend]
            else:
                buttonList += [self.txt.continue_with_bot]
            buttonList += [self.txt.request_draw, self.txt.resign]
        else:
            buttonList = [self.txt.new_game, self.txt.settings]

        for buttonTxt in buttonList:
            pygame.draw.rect(self.win, self.theme.menuBtnCLR, ((MenuStartX + MenuBtnLeftPad, txtY),
                                                               (MenuBtnWidth, MenuBtnHeight)), 0, 8)
            self.drawText(buttonTxt, self.sizes.menu_btn_size, txtX, txtY, self.theme.menuBtnTxtCLR, centre='X')
            txtY += MenuBtnHeight + btnPadding

        # Placing Quit button at end.
        txtY = MenuStartY + MenuLenY - btnPadding - MenuBtnHeight
        pygame.draw.rect(self.win, self.theme.menuBtnCLR, ((MenuBtnLeftPad, txtY), (MenuBtnWidth, MenuBtnHeight)), 0, 8)
        self.drawText(self.txt.quit, self.sizes.menu_btn_size, txtX, txtY, self.theme.menuBtnTxtCLR, centre='X')
        txtY += MenuBtnHeight + btnPadding

    def drawCoordinates(self):
        font = pygame.font.Font(self.txt.coordFont, 20)
        for number in coordinates.keys():
            if number % 2:
                clr = self.theme.lightCLR
            else:
                clr = self.theme.darkCLR

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

    def showPiece(self, piece, row, col):
        checkX = BoardStartX + padding + col * SquareDimen
        checkY = BoardStartY + padding + abs(7 - row) * SquareDimen
        X = checkX + (SquareDimen - PieceDimen) // 2
        Y = checkY + (SquareDimen - PieceDimen) // 2

        if piece == 'PREV_POS':
            pygame.draw.rect(self.win, self.theme.prevCLR, ((checkX, checkY), (SquareDimen, SquareDimen)))
        elif piece == 'NEW_POS':
            pygame.draw.rect(self.win, self.theme.newCLR, ((checkX, checkY), (SquareDimen, SquareDimen)))
        elif piece == 'TAKE':
            pygame.draw.circle(self.win, self.theme.takeCLR, (checkX + SquareDimen // 2, checkY + SquareDimen // 2),
                               SquareDimen // 2, 7)
        elif piece == 'MOVE':
            pygame.draw.circle(self.win, self.theme.moveCLR, (checkX + SquareDimen // 2, checkY + SquareDimen // 2),
                               SquareDimen // 9)
        elif piece == 'CASTLE':
            pygame.draw.circle(self.win, self.theme.castleCLR, (checkX + SquareDimen // 2, checkY + SquareDimen // 2),
                               SquareDimen // 9)
        elif piece == 'SELECT':
            pygame.draw.rect(self.win, self.theme.selectCLR, ((checkX, checkY), (SquareDimen, SquareDimen)))

        elif piece == 'P':
            self.win.blit(WHITE_PAWN, (X, Y))
        elif piece == 'p':
            self.win.blit(BLACK_PAWN, (X, Y))

        elif piece == 'K':
            if self.chessBoard.is_check() and self.chessBoard.turn:
                pygame.draw.rect(self.win, self.theme.checkCLR, ((checkX, checkY), (SquareDimen, SquareDimen)))
            self.win.blit(WHITE_KING, (X, Y))
        elif piece == 'k':
            if self.chessBoard.is_check() and not self.chessBoard.turn:
                pygame.draw.rect(self.win, self.theme.checkCLR, ((checkX, checkY), (SquareDimen, SquareDimen)))
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
        pygame.draw.rect(self.win, self.theme.lightCLR, (P1StartX, P1StartY, P1LenX, P1LenY))
        pad = int(P1LenY * 0.1)
        if turn:
            pygame.draw.rect(self.win, self.theme.turnCLR, (P1StartX, P1StartY, P1LenY, P1LenY))
        pygame.draw.rect(self.win, self.theme.darkCLR, (P1StartX + pad, P1StartY + pad, SquareDimen, SquareDimen))
        self.win.blit(WHITE_KING, (P1StartX + pad, P1StartY + pad))

        if self.vsAI and self.aiColor == CHESS_WHITE:
            self.drawText(self.txt.chess_bot, self.sizes.player_name, P1StartX + 3 * pad + SquareDimen,
                          P1StartY + padding, self.theme.darkCLR, font=self.txt.fontBold)
            if turn and not self.analysis:
                self.drawText(self.txt.i_am_thinking, self.sizes.think_msg, P1StartX + 3 * pad + SquareDimen,
                              P1StartY + 0.7 * SquareDimen, self.theme.thinkMsgFgCLR, self.theme.thinkMsgBgCLR,
                              font=self.txt.fontBold)
        else:
            self.drawText(self.p1Name, self.sizes.player_name, P1StartX + 3 * pad + SquareDimen,
                          P1StartY + (padding + SquareDimen) // 2,
                          self.theme.darkCLR, centre='Y', font=self.txt.fontBold)

        # self.drawText(self.p1Rating, 22, P1StartX + 3 * pad + SquareDimen, P1StartY + 4 * pad,
        # RatingFC, RatingBC, font=gameFontBold)

    def drawPlayer2(self, turn=False):
        pygame.draw.rect(self.win, self.theme.darkCLR, (P2StartX, P2StartY, P2LenX, P2LenY))
        pad = int(P2LenY * 0.1)
        if turn:
            pygame.draw.rect(self.win, self.theme.turnCLR, (P2StartX, P2StartY, P1LenY, P1LenY))
        pygame.draw.rect(self.win, self.theme.lightCLR, (P2StartX + pad, P2StartY + pad, SquareDimen, SquareDimen))
        self.win.blit(BLACK_KING, (P2StartX + pad, P2StartY + pad))

        if self.vsAI and self.aiColor == CHESS_BLACK:
            self.drawText(self.txt.chess_bot, self.sizes.player_name, P2StartX + 3 * pad + SquareDimen,
                          P2StartY + padding, self.theme.lightCLR, font=self.txt.fontBold)
            if turn and not self.analysis:
                self.drawText(self.txt.i_am_thinking, self.sizes.think_msg, P2StartX + 3 * pad + SquareDimen,
                              P2StartY + 0.7 * SquareDimen, self.theme.thinkMsgFgCLR, self.theme.thinkMsgBgCLR,
                              font=self.txt.fontBold)
        else:
            self.drawText(self.p2Name, self.sizes.player_name, P2StartX + 3 * pad + SquareDimen,
                          P2StartY + (padding + SquareDimen) // 2,
                          self.theme.lightCLR, centre='Y', font=self.txt.fontBold)

        # self.drawText(self.p2Rating, 22, P2StartX + 3 * pad + SquareDimen, P2StartY + 4 * pad,
        # RatingFC, RatingBC, font=gameFontBold)

    def drawPlayers(self):
        if self.chessBoard.turn:
            self.drawPlayer1(turn=True)
            self.drawPlayer2()
        else:
            self.drawPlayer1()
            self.drawPlayer2(turn=True)

    def isGameEnd(self):
        if self.analysis:
            return

        # Checkmate
        if self.chessBoard.is_checkmate():

            # Black won by checkmate.
            if self.chessBoard.turn:
                self.showDialog(self.txt.checkmate_msg_b, pBtn=(self.txt.new_game, self.newGame),
                                nBtn=(self.txt.analyse, self.analyse))

            # White won by checkmate.
            else:
                self.showDialog(self.txt.checkmate_msg_w, pBtn=(self.txt.new_game, self.newGame),
                                nBtn=(self.txt.analyse, self.analyse))

        # Draw by Threefold repetition.
        elif self.chessBoard.draw_by_threefold_repetition():
            self.showDialog(self.txt.threefold_rep_msg, pBtn=(self.txt.new_game, self.newGame),
                            nBtn=(self.txt.analyse, self.analyse))

        # Draw by Insufficient material.
        elif self.chessBoard.draw_by_insufficient_material():
            self.showDialog(self.txt.insufficient_mat_msg, pBtn=(self.txt.new_game, self.newGame),
                            nBtn=(self.txt.analyse, self.analyse))

        # Draw by Stalemate.
        elif self.chessBoard.draw_by_stalemate():
            self.showDialog(self.txt.stalemate_msg, pBtn=(self.txt.new_game, self.newGame),
                            nBtn=(self.txt.analyse, self.analyse))

        # Win by resignation.
        elif self.chessBoard.win_by_resignation():
            # Black won by resignation.
            if self.chessBoard.winner == CHESS_BLACK:
                self.showDialog(self.txt.resign_msg_b, pBtn=(self.txt.new_game, self.newGame),
                                nBtn=(self.txt.analyse, self.analyse))

            # White won by resignation.
            else:
                self.showDialog(self.txt.resign_msg_w, pBtn=(self.txt.new_game, self.newGame),
                                nBtn=(self.txt.analyse, self.analyse))

        # Draw accepted.
        elif self.chessBoard.draw_accepted:
            self.showDialog(self.txt.draw_accept_msg, pBtn=(self.txt.new_game, self.newGame),
                            nBtn=(self.txt.analyse, self.analyse))

        elif self.chessBoard.draw_rejected:
            self.chessBoard.draw_rejected = False
            self.showDialog(self.txt.draw_reject_msg)

    def drawEvalBar(self):
        if self.analysis:
            pygame.draw.rect(self.win, self.theme.borderCLR, (EvalBarStartX, EvalBarStartY, EvalBarLenX, EvalBarLenY))
            # here, 18 = fontSize, 9 = fontSize/2, 27 = fontSize*(3/2)
            s = self.sizes.coord
            yLen = HEIGHT - 2 * padding - s - s - s//2 - s//2
            self.drawText(self.chessBoard.p2_adv, s, EvalBarStartX + EvalBarLenX // 2,
                          padding + s//2, self.theme.darkCLR, centre=True)
            self.drawText(self.chessBoard.p1_adv, s, EvalBarStartX + EvalBarLenX // 2,
                          HEIGHT - padding - s//2, self.theme.lightCLR, centre=True)
            DarkLen = int(yLen * (100 - self.chessBoard.win_percent) / 100)
            pygame.draw.rect(self.win, self.theme.darkCLR,
                             (EvalBarStartX + padding, padding + s*3//2, EvalBarWidth, DarkLen))
            pygame.draw.rect(self.win, self.theme.lightCLR,
                             (EvalBarStartX + padding, padding + s*3//2 + DarkLen, EvalBarWidth, yLen - DarkLen))
        else:
            pygame.draw.rect(self.win, self.theme.darkCLR,
                             (EvalBarStartX + padding, EvalBarStartY, EvalBarLenX - padding, EvalBarLenY))

    def drawInformation(self):
        X, Y, LenX, LenY = InfoStartX, InfoStartY, InfoLenX, InfoLenY
        try:
            userMove = self.chessBoard.moveList[-1]
        except IndexError:
            userMove = None
        bestMove = self.chessBoard.bestPrevMove
        if self.analysis:
            pygame.draw.rect(self.win, self.theme.lightCLR, (InfoStartX, InfoStartY, InfoLenX, InfoLenY))

            self.drawText(self.txt.analyse, 40, X+LenX//2, Y+padding//2, CHESS_BLACK, centre='X')
            if userMove:
                self.drawText("Your Move : " + userMove, 25, X + padding, Y + LenY // 2, CHESS_BLACK,
                              font=self.txt.engFont, centre='Y')
            if bestMove:
                self.drawText("Best Move : " + bestMove, 25, X + padding, Y + LenY - 50, CHESS_BLACK,
                              font=self.txt.engFont)
        else:
            pygame.draw.rect(self.win, self.theme.darkCLR, (InfoStartX, InfoStartY, InfoLenX, InfoLenY))

    def drawFEN(self):
        pygame.draw.rect(self.win, self.theme.fenCLR, (FENStartX, FENStartY, FENLenX, FENLenY))
        whiteMoveList = []
        blackMoveList = []
        for x in range(len(self.chessBoard.moveList)):
            if x % 2 == 0:
                whiteMoveList.append(self.chessBoard.moveList[x])
            else:
                blackMoveList.append(self.chessBoard.moveList[x])

        pygame.draw.rect(self.win, self.theme.fenCLR, (FENStartX, FENStartY, FENLenX, FENLenY))
        self.fruit.updatemainList(blackMoveList)
        self.fruit.UpdateData(whiteMoveList)

    def analyse(self):
        self.analysis = True
        self.vsAI = False
        self.aiColor = None

    def newGame(self):
        self.chessBoard.__init__(self.chessBoard.Board_type)
        p = self.preferences
        self.__init__(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])

    def menuClick(self, pos):
        row, col = pos
        if MenuStartX < row < MenuStartX + MenuLenX and MenuStartY < col < MenuStartY + MenuLenY:
            centre = MenuStartX + MenuLenX // 2

            # Backward and forward move
            if 0 < col - MenuStartY - btnPadding < ArrowBtnLenY:
                if centre - btnPadding - ArrowBtnLenX < row < centre - btnPadding:
                    self.clearUIMoves()
                    if self.vsAI and not self.analysis:
                        self.chessBoard.move_back()
                    self.chessBoard.move_back()
                    self.updateBoard()

                elif 0 < row - centre - btnPadding < ArrowBtnLenX:
                    self.clearUIMoves()
                    if self.vsAI and not self.analysis:
                        self.chessBoard.move()
                    self.chessBoard.move()
                    self.updateBoard()
            Y = MenuStartY + btnPadding * 3 + MenuBtnHeight

            if 0 < row - MenuStartX - MenuBtnLeftPad < MenuBtnWidth:

                if not self.analysis:
                    # Quit
                    if MenuStartY + MenuLenY - btnPadding - MenuBtnHeight < col < MenuStartY + MenuLenY - btnPadding:
                        self.showDialog(self.txt.quit_msg,
                                        pBtn=(self.txt.yes, self.quit), nBtn=(self.txt.no, self.doNothing))

                    # New Game.
                    if Y < col < Y + MenuBtnHeight:
                        self.showDialog(self.txt.new_game_msg, pBtn=(self.txt.yes, self.newGame),
                                        nBtn=(self.txt.no, self.doNothing))
                    Y += btnPadding + MenuBtnHeight

                    # Game saved.
                    if Y < col < Y + MenuBtnHeight:
                        self.saveBoard()
                        self.showDialog(self.txt.game_saved_msg)
                    Y += btnPadding + MenuBtnHeight

                    # Settings.
                    if Y < col < Y + MenuBtnHeight:
                        print("--> Settings not implemented. <--")
                    Y += btnPadding + MenuBtnHeight

                    # Continue with friend/bot.
                    if Y < col < Y + MenuBtnHeight:
                        if self.vsAI:
                            self.showDialog(self.txt.cont_with_friend_qn,
                                            pBtn=(self.txt.yes, self.switchPlayerAndAI),
                                            nBtn=(self.txt.no, self.doNothing))
                        else:
                            self.showDialog(self.txt.cont_with_bot_qn,
                                            pBtn=(self.txt.yes, self.switchPlayerAndAI),
                                            nBtn=(self.txt.no, self.doNothing))
                    Y += btnPadding + MenuBtnHeight

                    # Request draw.
                    if Y < col < Y + MenuBtnHeight:
                        self.showDialog(self.txt.req_draw_qn,
                                        pBtn=(self.txt.yes, self.chessBoard.request_draw),
                                        nBtn=(self.txt.no, self.doNothing))
                    Y += btnPadding + MenuBtnHeight

                    # resign.
                    if Y < col < Y + MenuBtnHeight:
                        self.showDialog(self.txt.resign_qn, pBtn=(self.txt.yes, self.chessBoard.resign),
                                        nBtn=(self.txt.no, self.doNothing))

                else:
                    # Quit
                    if MenuStartY + MenuLenY - btnPadding - MenuBtnHeight < col < MenuStartY + MenuLenY - btnPadding:
                        self.showDialog(self.txt.quit_no_save_msg,
                                        pBtn=(self.txt.yes, self.quit), nBtn=(self.txt.no, self.doNothing))

                    # New Game.
                    if Y < col < Y + MenuBtnHeight:
                        self.showDialog(self.txt.new_game_qn, pBtn=(self.txt.yes, self.newGame),
                                        nBtn=(self.txt.no, self.doNothing))
                    Y += btnPadding + MenuBtnHeight

                    # Settings.
                    if Y < col < Y + MenuBtnHeight:
                        print("--> Settings not implemented. <--")

    def switchPlayerAndAI(self):
        # Ai started parameter is handled in while loop of play.py
        message = self.txt.switching + ' '
        if self.vsAI:
            self.aiColor = None
            self.vsAI = False
            if self.chessBoard.turn:
                message += self.txt.chess_bot_with + ' ' + self.p2Name + ' ' + self.txt.exclamation
            else:
                message += self.txt.chess_bot_with + ' ' + self.p1Name + ' ' + self.txt.exclamation
        else:
            self.vsAI = 'MEDIUM'
            if self.chessBoard.turn:
                self.aiColor = CHESS_BLACK
                self.aiTurn = False
                message += self.p2Name + self.txt.with_chess_bot + ' ' + self.txt.exclamation
            else:
                self.aiColor = CHESS_WHITE
                self.aiTurn = True
                message += self.p1Name + self.txt.with_chess_bot + ' ' + self.txt.exclamation

        self.showDialog(message)

    def playAiMove(self, move):
        self.chessBoard.move(move)
        self.updateBoard()

    def click(self, pos):
        pos = getBoardRowColFromPos(pos)
        if pos != (-1, -1):
            col, row = pos
            row = abs(7 - row)
        else:
            self.clearUIMoves()
            return

        if self.promotionMove:
            if row == 3 and col == 3:
                self.promotionMove = re_sub('=.', '=B', self.promotionMove)
                self.chessBoard.move(self.promotionMove)
            if row == 3 and col == 4:
                self.promotionMove = re_sub('=.', '=N', self.promotionMove)
                self.chessBoard.move(self.promotionMove)
            if row == 4 and col == 3:
                self.promotionMove = re_sub('=.', '=Q', self.promotionMove)
                self.chessBoard.move(self.promotionMove)
            if row == 4 and col == 4:
                self.promotionMove = re_sub('=.', '=R', self.promotionMove)
                self.chessBoard.move(self.promotionMove)
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
                        self.promotionMove = self.moveLoc[(row, col)]
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

        # Selecting AIs pieces is not allowed.
        elif clickedPiece.color == self.aiColor and not self.selectedPiece:
            return

        # Clicked piece is of opponent's color.
        elif clickedPiece.color != my_color:
            if self.selectedPiece:
                if (row, col) in self.takesLoc.keys():
                    if '=' in self.takesLoc[(row, col)]:
                        self.promotionMove = self.takesLoc[(row, col)]
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
            moves = clickedPiece.get_valid_moves(board, board.en_passants[board.moveCount - 1])
        else:
            moves = clickedPiece.get_valid_moves(board)
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

        for pos in self.chessBoard.prev_pos:
            self.showPiece('PREV_POS', pos[0], pos[1])

        for pos in self.chessBoard.new_pos:
            self.showPiece('NEW_POS', pos[0], pos[1])

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
            pygame.draw.rect(self.win, self.theme.promotionCLR, (X, Y, 2 * SquareDimen, 2 * SquareDimen))
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

    def drawText(self, text, size, txtX, txtY, color, colorBg=None, font=None, centre=False):
        if font is None:
            font = self.txt.font
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

    def quit(self):
        if self.analysis:
            self.delete_saved_board()
        else:
            self.saveBoard()
        self.running = False

    def saveBoard(self):
        with open(brdFileName, 'wb') as brdFile:
            pickle.dump(self.chessBoard, brdFile)

    def delete_saved_board(self):
        if os.path.exists(brdFileName):
            os.remove(brdFileName)
            self.chessBoard = None

    def doNothing(self):
        pass

    def showDialog(self, text, winTitle=None, pBtn=None, nBtn=None, sleepTime=1):
        if winTitle is None:
            winTitle = self.txt.chess
        self.dialog = AlertDialog(self.win, text, self.theme.alertFgCLR, self.theme.alertBgCLR, self.txt.font,
                                  winTitle, self.sizes.alert_sizes, pBtn, nBtn)
        self.dialog.show()
        if pBtn == nBtn is None:
            time.sleep(sleepTime)
            self.removeDialog()

    def dialogClick(self, pos):
        if self.dialog.pBtn and pygame.Rect.collidepoint(self.dialog.pBtnRect, pos):
            self.dialog.pBtn[1]()
        elif self.dialog.nBtn and pygame.Rect.collidepoint(self.dialog.nBtnRect, pos):
            self.dialog.nBtn[1]()
        self.removeDialog()

    def removeDialog(self):
        self.dialog = None
        # noinspection PyBroadException
        try:
            self.updateBoard()
        except:
            pass
