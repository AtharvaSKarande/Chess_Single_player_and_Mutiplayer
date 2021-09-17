import pygame

import Chess
from Game.ui import UI
from Game.values.dimens import WIDTH, HEIGHT, TitleLenX

FPS = 60
win = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Chess: Single player and Multiplayer')


def start():
    running = True
    clock = pygame.time.Clock()
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
            running = False
    pygame.quit()


if __name__ == "__main__":
    start()
