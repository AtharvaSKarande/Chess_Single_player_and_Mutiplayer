import time

import pygame
from Game.ui import UI
from Game.constants import WIDTH, HEIGHT, FPS
import Chess

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess: Single player and Multiplayer')


def start():
    running = True
    clock = pygame.time.Clock()
    chessBoard = Chess.chessBoard()
    displayUI = UI(win, chessBoard)
    displayUI.drawDisplay()
    # SRrecog = SpeechRecogniser()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                displayUI.click(pos)
        print(displayUI.chessBoard.get_all_valid_moves())
        if displayUI.isGameEnd():
            running = False
    pygame.quit()


if __name__ == "__main__":
    start()
