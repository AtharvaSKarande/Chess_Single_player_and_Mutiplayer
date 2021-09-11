import pygame

# Window size of user
pygame.init()
info = pygame.display.Info()
WIDTH, HEIGHT = int(info.current_w), int(info.current_h * 0.92)

padding = 16

coordinates = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

# Dimensions of square
SquareDimen = int((HEIGHT - 2 * padding) / 8)
# Dimensions of pieces
PieceDimen = int(SquareDimen * 0.95)

# Menu tab
MenuStartX = 0
MenuStartY = 0
MenuLenX = int(WIDTH * 0.25)
MenuLenY = HEIGHT * 0.7

# Board
BoardStartX = MenuStartX + MenuLenX
BoardStartY = 0
BoardLen = HEIGHT

# Player 1
P1StartX = 0
P1StartY = HEIGHT * 0.7
P1LenX = MenuLenX
P1LenY = HEIGHT * 0.15

# Player 2
P2StartX = 0
P2StartY = HEIGHT * 0.85
P2LenX = MenuLenX
P2LenY = HEIGHT * 0.16

# Evaluation Bar (Temporarily, eval bar is not displayed.)
EvalBarStartX = BoardStartX + BoardLen - padding
EvalBarStartY = 0
EvalBarWidth = 25
EvalBarLenX = padding     # 16 + EvalBarWidth + 16
EvalBarLenY = HEIGHT

# Previous moves tab
FENStartX = EvalBarStartX + EvalBarLenX
FENStartY = 0
FENLenX = WIDTH - FENStartX
FENLenY = HEIGHT
