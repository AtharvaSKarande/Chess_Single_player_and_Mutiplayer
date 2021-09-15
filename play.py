import pygame

import Chess
from Game.ui import UI
from Game.values.dimens import WIDTH, HEIGHT

FPS = 60
win = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
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
        # print(displayUI.chessBoard.en_passants)
        if displayUI.isGameEnd():
            running = False
    pygame.quit()


if __name__ == "__main__":
    start()
