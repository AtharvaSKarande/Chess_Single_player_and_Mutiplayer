import os
import pickle

import Chess
from Game import UI
from ChessAI import AI
from Game.values.dimens import *
from Game.values.assets import brdFileName

FPS = 60
win = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Chess: Single player and Multiplayer')


class Play:
    def __init__(self):
        self.chessBoard = None
        self.displayUI = None
        self.ai = None

    def start(self, vsAI, aiColor, theme, p1Name="Player 1", p2Name="Player 2"):
        clock = pygame.time.Clock()
        self.assignChessBoard()

        self.displayUI = UI(win, self.chessBoard, vsAI=vsAI, aiColor=aiColor, gameTheme=theme, p1Name=p1Name,
                            p2Name=p2Name)
        self.displayUI.listview.setOnItemSelected(self.OnItemClick)
        self.displayUI.drawDisplay()

        while self.displayUI.running:
            clock.tick(FPS)
            for event in pygame.event.get():
                self.displayUI.listview.eventHandler(event)

                if event.type == pygame.QUIT:
                    self.displayUI.running = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.displayUI.dialog:
                        self.displayUI.dialogClick(pos)
                    else:
                        if pos[0] < TitleLenX:
                            self.displayUI.menuClick(pos)
                        else:
                            self.displayUI.click(pos)

            if self.displayUI.vsAI and self.displayUI.aiMove and \
                    self.displayUI.chessBoard.turn == self.displayUI.aiTurn:
                # Move taken from AI.
                self.displayUI.playAiMove(self.displayUI.aiMove)
                self.displayUI.aiMove = None
                self.displayUI.aiStarted = False

            if self.displayUI.vsAI and not self.displayUI.aiStarted and self.displayUI.running and \
                    self.displayUI.aiTurn == self.displayUI.chessBoard.turn and \
                    self.displayUI.aiMove is None and not self.displayUI.analysis:
                # Start AI thread.
                self.displayUI.aiStarted = True
                self.ai = AI(self.displayUI)
                self.ai.start()

            if not self.displayUI.vsAI and self.displayUI.aiStarted:
                # Stop AI thread.
                self.displayUI.aiStarted = False
                self.ai.join()

        self.displayUI.quit()

    def assignChessBoard(self):
        if os.path.exists(brdFileName):
            with open(brdFileName, "rb") as savedBrd:
                self.chessBoard = pickle.load(savedBrd)
        else:
            self.chessBoard = Chess.chessBoard()

    # noinspection PyUnusedLocal
    def OnItemClick(self, x, y, W, Ih, pos):
        if W / 6 < x < W / 6 + 70:
            pos = 2 * pos
            length = len(self.chessBoard.moveList)
            for hold in range(pos, length - 1):
                self.chessBoard.move_back()
            self.displayUI.updateBoard()

        elif W / 2 < x < W / 2 + 70:
            pos = 2 * pos + 1
            length = len(self.chessBoard.moveList)
            for hold in range(pos, length - 1):
                self.chessBoard.move_back()
            self.displayUI.updateBoard()


if __name__ == "__main__":
    playGame = Play()
    playGame.start(vsAI=False, aiColor=None, theme="DEFAULT")
