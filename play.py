import pickle

import pygame
import os
import Chess
from Game import UI
from Game.values.dimens import WIDTH, HEIGHT, TitleLenX
from Game.values.string import brdFileName

FPS = 60
win = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Chess: Single player and Multiplayer')

class Play:
    def __init__(self):
        self.chessBoard = None

    def start(self):
        running = True
        clock = pygame.time.Clock()
        self.assignChessBoard()
        displayUI = UI(win, self.chessBoard)
        displayUI.drawDisplay()

        while running:
            clock.tick(FPS)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if displayUI.dialog:
                        displayUI.dialogClick(pos)
                    else:
                        if pos[0] < TitleLenX:
                            running = displayUI.menuClick(pos)
                        else:
                            displayUI.click(pos)

            if displayUI.isGameEnd():
                self.delete_saved_board()
                running = False
        pygame.quit()

    def assignChessBoard(self):
        if os.path.exists(brdFileName):
            with open(brdFileName, "rb") as savedBrd:
                self.chessBoard = pickle.load(savedBrd)
        else:
            self.chessBoard = Chess.chessBoard()

    def delete_saved_board(self):
        if os.path.exists(brdFileName):
            os.remove(brdFileName)
            self.chessBoard = None


if __name__ == "__main__":
    playGame = Play()
    playGame.start()
