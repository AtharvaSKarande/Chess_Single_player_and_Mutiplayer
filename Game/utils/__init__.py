from Game.values.dimens import *
from Game.values.colors import CHESS_WHITE


class AlertDialog:
    def __init__(self, win, alertText, fgCLR, bgCLR, font, title='Chess', positiveBtn=None, negativeBtn=None):
        self.win = win
        self.alertText = alertText
        self.title = title
        self.fgCLR = fgCLR
        self.bgCLR = bgCLR
        self.font = font
        self.pBtn = positiveBtn
        self.nBtn = negativeBtn
        self.pBtnRect = None
        self.nBtnRect = None

    def show(self):
        pygame.draw.rect(self.win, self.bgCLR, ((AlertDialogStartX, AlertDialogStartY),
                                                (AlertDialogLenX, AlertDialogLenY)),
                         border_radius=DialogTitleHeight // 2)
        pygame.draw.rect(self.win, self.fgCLR,
                         ((DialogInX, DialogInY), (DialogInLenX, DialogInLenY)),
                         border_bottom_left_radius=DialogTitleHeight // 2,
                         border_bottom_right_radius=DialogTitleHeight // 2)

        self.drawText(self.title, 50, AlertDialogStartX + AlertDialogLenX // 2, AlertDialogStartY +
                      (dialogPad + DialogTitleHeight) // 2, CHESS_WHITE, centre='XY')

        if '*' not in self.alertText:
            self.drawText(self.alertText, 40, DialogInX + DialogInLenX // 2, DialogInY + SquareDimen,
                          CHESS_WHITE, centre=True)
        else:
            texts = self.alertText.split('*')
            length = SquareDimen // (len(texts) + (len(texts) % 2))
            for txt in texts:
                self.drawText(txt, 30, DialogInX + DialogInLenX // 2, DialogInY + length, CHESS_WHITE, centre=True)
                length += SquareDimen // 2

        btnX = DialogInX + int(0.125 * DialogInLenX)
        btnLenY = int(DialogInLenY * 0.2)
        btnY = DialogInY + int(0.7 * DialogInLenY)
        if self.nBtn:
            btnLenX = min(int(1.5 * SquareDimen), max(SquareDimen, 30 * (len(self.nBtn) + 2)))
            self.nBtnRect = pygame.draw.rect(self.win, CHESS_WHITE, ((btnX, btnY), (btnLenX, btnLenY)),
                                             border_radius=15)
            self.drawText(self.nBtn[0], 20, btnX + btnLenX // 2, btnY + btnLenY // 2, (0, 0, 0), centre=True)
        if self.pBtn:
            btnLenX = min(int(1.5 * SquareDimen), max(SquareDimen, 30 * (len(self.pBtn) + 2)))
            self.pBtnRect = pygame.draw.rect(self.win, CHESS_WHITE, ((btnX + DialogInLenX // 2, btnY),
                                                                     (btnLenX, btnLenY)), border_radius=15)
            self.drawText(self.pBtn[0], 20, btnX + DialogInLenX // 2 + btnLenX // 2, btnY + btnLenY // 2, (0, 0, 0),
                          centre=True)
        pygame.display.update()

    def drawText(self, text, size, txtX, txtY, color, colorBg=None, centre=False):
        Txt = pygame.font.Font(self.font, size).render(text, True, color, colorBg)
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

class Language:
    def __init__(self, language):
        self.language = language
        self.font = "Assets/product_sans_regular.ttf"
        self.fontBold = "Assets/product_sans_bold.ttf"

        self.p1Name = "Player 1"
        self.p2Name = "Player 2"

        self.chess = "Chess"
        self.chess_bot = "Chess Bot"
        self.yes = "Yes"
        self.no = "No"

        self.new_game = "New Game"
        self.save_game = "Save Game"
        self.settings = "Settings"
        self.continue_with_friend = "Continue with friend"
        self.continue_with_bot = "Continue with bot"
        self.request_draw = "Request Draw"
        self.resign = "Resign"
        self.quit = "Quit"
        self.analyse = "Analyse"
        self.i_am_thinking = "I am thinking..."

        self.checkmate_msg_b = "Checkmate*Black Won !"
        self.checkmate_msg_w = "Checkmate*White Won !"
        self.threefold_rep_msg = "Game drawn by*Threefold repetition !"
        self.insufficient_mat_msg = "Game drawn by*Insufficient material !"
        self.stalemate_msg = "Game drawn by*Stalemate !"
        self.resign_msg_b = "Resignation*Black won !"
        self.resign_msg_w = "Resignation*White won !"
        self.draw_accept_msg = "Game drawn !*Draw accepted."

        self.quit_msg = "Do you really want to quit?*The game will be saved."
        self.new_game_msg = "Do you really want to*start a new game?"
        self.game_saved_msg = "Game Saved."

        self.cont_with_friend_qn = "Do you want to continue*the game with the friend?"
        self.cont_with_bot_qn = "Do you want to continue*the game with the bot?"
        self.req_draw_qn = "Do you really want to*request a draw?"
        self.resign_qn = "Do you really want to*resign form game?"
        self.quit_no_save_msg = "Do you really want to quit?*The game will not be saved !!"
        self.new_game_qn = "Do you really want to*start a new game?"

        self.switching = "*Switching"
        self.chess_bot_with = "Chess Bot*with"
        self.with_chess_bot = "*with Chess Bot"
        self.exclamation = "!"

        self.setLanguage()

    def setLanguage(self):
        if self.language == 'HINDI':
            self.font = "Assets/shivaji.ttf"
            self.fontBold = "Assets/shivaji.ttf"

            self.p1Name = "iKlaaDI 1"
            self.p2Name = "iKlaaDI 2"

            self.chess = "SatrMja"
            self.chess_bot = "SatrMja baa^T"
            self.yes = "ha"
            self.no = "nahIM"

class Theme:
    def __init__(self, theme):
        self.title = theme

        self.lightCLR, self.darkCLR = (238, 238, 210), (118, 150, 86)
        self.borderCLR = (50, 50, 50)
        self.turnCLR = (0, 225, 0)
        self.menuBtnTxtCLR = (0, 0, 0)
        self.thinkMsgFgCLR = (255, 255, 255)
        self.thinkMsgBgCLR = (255, 0, 0)
        self.checkCLR, self.takeCLR, self.moveCLR = (255, 0, 0), (255, 0, 0), (255, 0, 0)
        self.castleCLR, self.selectCLR, self.promotionCLR = (50, 50, 255), (200, 255, 0), (100, 100, 255)
        self.alertFgCLR, self.alertBgCLR = (150, 150, 150), (100, 100, 100)

        self.setTheme()

        self.menuCLR, self.menuBtnCLR = self.darkCLR, self.lightCLR
        self.evalTxtBgCLR = self.lightCLR
        self.fenCLR = self.darkCLR

    def setTheme(self):
        if self.title == 'ORANGE':
            self.lightCLR = (240, 217, 181)
            self.darkCLR = (181, 136, 99)
