import pickle

import pygame
import os
import Chess
from Game.ui import UI
from Game.values.dimens import WIDTH, HEIGHT, TitleLenX
from Game.values.string import brdFileName

FPS = 60
win = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Chess: Single player and Multiplayer')


def start():
    running = True
    clock = pygame.time.Clock()
    if os.path.exists(brdFileName):
        with open(brdFileName, "rb") as savedBrd:
            chessBoard = pickle.load(savedBrd)
    else:
        chessBoard = Chess.chessBoard()
    displayUI = UI(win, chessBoard)
    displayUI.drawDisplay()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] < TitleLenX:
                    running = displayUI.menuClick(pos)
                else:
                    displayUI.click(pos)

        if displayUI.isGameEnd():
            delete_saved_board()
            running = False
    pygame.quit()


def delete_saved_board():
    if os.path.exists(brdFileName):
        os.remove(brdFileName)


if __name__ == "__main__":
    start()
