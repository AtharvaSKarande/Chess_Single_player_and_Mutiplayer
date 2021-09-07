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
    MOVES = ['P_f2_f4', 'P_g7_g5', 'P_f4_g5xP', 'P_f7_f5', 'P_g5_f6xP', 'B_f8_g7', 'P_f6_g7xB', 'K_e8_f7',
             'P_g7_h8xR=Q', 'P_a7_a5', 'N_g1_h3', 'R_a8_a6', 'P_g2_g4', 'N_b8_c6', 'B_f1_g2', 'N_c6_d4', 'O-O']

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                displayUI.click(pos)

        """
           Checking : (Use this in command line)
        # * 1 -> pop element from MOVES. and play. ( Don't use of previous moves exist.
        #       it will crash later as moves and board will not remain in sync.)
        # * 2 -> play next move (available when you have used at least one previous move).
        # * any other -> Moves back.
        """

        t = input()
        if t == '1':
            if MOVES:
                move = MOVES.pop(0)
                displayUI.chessBoard.move(move, debug=True)
            else:
                break
        elif t == "2":
            move = None
            displayUI.chessBoard.move(move, debug=True)
        else:
            displayUI.chessBoard.move_back()

        # displayUI.chessBoard.move(move, debug=True)
        displayUI.updateBoard()
        if displayUI.isGameEnd():
            running = False
    pygame.quit()


if __name__ == "__main__":
    start()
