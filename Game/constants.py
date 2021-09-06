import pygame

# USER WINDOW SIZE
pygame.init()
info = pygame.display.Info()
WIDTH, HEIGHT = int(info.current_w), int(info.current_h * 0.92)
padding = 16
FPS = 60
gameFont = "Assets/product_sans_regular.ttf"
gameFontBold = "Assets/product_sans_bold.ttf"
# int(int(info.current_h * 0.85) / 8) * 8, int(info.current_h * 0.9)
CHESS_WHITE = (238, 238, 210)
CHESS_BLACK = (118, 150, 86)

MenuColor = (200, 0, 0)
MenuStartX = 0
MenuStartY = 0
MenuLenX = int(WIDTH * 0.25)
MenuLenY = HEIGHT * 0.7

BoardLight = (238, 238, 210)  # (204, 127, 99)
BoardDark = (118, 150, 86)  # (81, 56, 80)
BoardStartX = MenuStartX + MenuLenX
BoardStartY = 0
BoardLen = HEIGHT

BorderColor = (50, 50, 50)
CheckColor = (255, 0, 0)

EvalBarStartX = BoardStartX + BoardLen - padding
EvalBarStartY = 0
EvalBarWidth = 25
EvalBarLenX = 16 + EvalBarWidth + 16
EvalBarLenY = HEIGHT

PreviousMoveStartX = EvalBarStartX + EvalBarLenX
PreviousMoveStartY = 0
PreviousMoveLenX = WIDTH - EvalBarStartX - EvalBarLenX
PreviousMoveLenY = HEIGHT
PreviousMoveColor = (0, 0, 0)

turnColor = (0, 225, 0)

P1Name = "Atharva S Karande"
P1Rating = " GM "
P1StartX = 0
P1StartY = HEIGHT * 0.7
P1LenX = MenuLenX
P1LenY = HEIGHT * 0.15

P2Name = "Carleson Magnus"
P2Rating = " GM "
P2StartX = 0
P2StartY = HEIGHT * 0.85
P2LenX = MenuLenX
P2LenY = HEIGHT * 0.16

RatingFC = (255, 255, 255)
RatingBC = (255, 0, 0)

coordinates = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

SquareDimen = int((HEIGHT - 2 * padding) / 8)

PieceDimen = int(SquareDimen * 0.95)

WHITE_PAWN = pygame.transform.scale(pygame.image.load('assets/wpawn.png'), (PieceDimen, PieceDimen))
WHITE_KING = pygame.transform.scale(pygame.image.load('assets/wking.png'), (PieceDimen, PieceDimen))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load('assets/wqueen.png'), (PieceDimen, PieceDimen))
WHITE_BISHOP = pygame.transform.scale(pygame.image.load('assets/wbishop.png'), (PieceDimen, PieceDimen))
WHITE_KNIGHT = pygame.transform.scale(pygame.image.load('assets/wknight.png'), (PieceDimen, PieceDimen))
WHITE_ROOK = pygame.transform.scale(pygame.image.load('assets/wrook.png'), (PieceDimen, PieceDimen))

BLACK_PAWN = pygame.transform.scale(pygame.image.load('assets/bpawn.png'), (PieceDimen, PieceDimen))
BLACK_KING = pygame.transform.scale(pygame.image.load('assets/bking.png'), (PieceDimen, PieceDimen))
BLACK_QUEEN = pygame.transform.scale(pygame.image.load('assets/bqueen.png'), (PieceDimen, PieceDimen))
BLACK_BISHOP = pygame.transform.scale(pygame.image.load('assets/bbishop.png'), (PieceDimen, PieceDimen))
BLACK_KNIGHT = pygame.transform.scale(pygame.image.load('assets/bknight.png'), (PieceDimen, PieceDimen))
BLACK_ROOK = pygame.transform.scale(pygame.image.load('assets/brook.png'), (PieceDimen, PieceDimen))

# CHESS_BG = pygame.transform.scale(pygame.image.load('Assets/ChessBG.png'), (WIDTH, HEIGHT))
