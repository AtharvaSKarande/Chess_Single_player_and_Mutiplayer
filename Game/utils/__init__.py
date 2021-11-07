from Game.values.dimens import *
from Game.values.colors import CHESS_WHITE


class AlertDialog:
    def __init__(self, win, alertText, fgCLR, bgCLR, text_font, title, text_sizes, positiveBtn=None, negativeBtn=None):
        self.win = win
        self.alertText = alertText
        self.title = title
        self.fgCLR = fgCLR
        self.bgCLR = bgCLR
        self.text_font = text_font
        self.text_sizes = text_sizes
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

        self.drawText(self.title, self.text_sizes[0], AlertDialogStartX + AlertDialogLenX // 2, AlertDialogStartY +
                      (dialogPad + DialogTitleHeight) // 2, CHESS_WHITE, centre='XY')

        if '*' not in self.alertText:
            self.drawText(self.alertText, self.text_sizes[1], DialogInX + DialogInLenX // 2, DialogInY + SquareDimen,
                          CHESS_WHITE, centre=True)
        else:
            texts = self.alertText.split('*')
            length = SquareDimen // (len(texts) + (len(texts) % 2))
            for txt in texts:
                self.drawText(txt, self.text_sizes[2], DialogInX + DialogInLenX // 2, DialogInY + length, CHESS_WHITE,
                              centre=True)
                length += SquareDimen // 2

        btnX = DialogInX + int(0.125 * DialogInLenX)
        btnLenY = int(DialogInLenY * 0.2)
        btnY = DialogInY + int(0.7 * DialogInLenY)
        if self.nBtn:
            btnLenX = min(int(1.5 * SquareDimen), max(SquareDimen, 30 * (len(self.nBtn) + 2)))
            self.nBtnRect = pygame.draw.rect(self.win, CHESS_WHITE, ((btnX, btnY), (btnLenX, btnLenY)),
                                             border_radius=15)
            self.drawText(self.nBtn[0], self.text_sizes[3], btnX + btnLenX // 2, btnY + btnLenY // 2, (0, 0, 0),
                          centre=True)
        if self.pBtn:
            btnLenX = min(int(1.5 * SquareDimen), max(SquareDimen, 30 * (len(self.pBtn) + 2)))
            self.pBtnRect = pygame.draw.rect(self.win, CHESS_WHITE, ((btnX + DialogInLenX // 2, btnY),
                                                                     (btnLenX, btnLenY)), border_radius=15)
            self.drawText(self.pBtn[0], self.text_sizes[3], btnX + DialogInLenX // 2 + btnLenX // 2,
                          btnY + btnLenY // 2, (0, 0, 0), centre=True)
        pygame.display.update()

    def drawText(self, text, size, txtX, txtY, color, colorBg=None, centre=False):
        Txt = pygame.font.Font(self.text_font, size).render(text, True, color, colorBg)
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

class FontSizes:
    def __init__(self, lang):
        self.lang = lang

        self.player_name = 36
        self.menu_btn_size = 25
        self.think_msg = 26
        self.coord = 18
        self.alert_sizes = [50, 40, 30, 20]   # Title, textLarge, textSmall, Btn
        self.setSizes()

    def setSizes(self):
        if self.lang == 'HINDI':
            self.player_name = 52
            self.think_msg = 32
            self.menu_btn_size = 32
            self.alert_sizes = [60, 50, 40, 35]

class Language:
    def __init__(self, language):
        self.language = language
        self.font = "Assets/product_sans_regular.ttf"
        self.fontBold = "Assets/product_sans_bold.ttf"
        self.coordFont = "Assets/product_sans_bold.ttf"
        self.engFont = "Assets/product_sans_regular.ttf"

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
        self.draw_reject_msg = "*Points doesn't match.*Draw Rejected."

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

        self.analysis = "Analysis"

        self.setLanguage()

    def setLanguage(self):
        if self.language == 'HINDI':
            self.font = "Assets/Shiv02.ttf"
            self.fontBold = "Assets/Shiv02.ttf"

            self.p1Name = "iKlaaDI 1"
            self.p2Name = "iKlaaDI 2"

            self.chess = "SatrMja"
            self.chess_bot = "SatrMja baa^T"
            self.yes = "ha"
            self.no = "nahIM"

            self.new_game = "nayaa Kola"
            self.save_game = "jatna kro"
            self.settings = "samaayaaojana"
            self.continue_with_friend = "daost ko saaqa jaarI rKoM"
            self.continue_with_bot = "baa^T ko saaqa jaarI rKoM"
            self.request_draw = "samaanata ko ilayao puCoM"
            self.resign = "har isvakaro"
            self.quit = "baMd kroM"
            self.analyse = "ivaSlaoYaNa"
            self.i_am_thinking = "maOM saaoca rha hM^U…"

            self.checkmate_msg_b = "maat*kalao isa@kaoM vaalaa ijata Ñ"
            self.checkmate_msg_w = "maat*safod isa@kaoM vaalaa ijata Ñ"
            self.threefold_rep_msg = "tIna gaunaa daohrava*Wara Kola samaana huAa^M Ñ"
            self.insufficient_mat_msg = "Apyaa-Pt saamaga`I*Wara Kola samaana huAa^M Ñ"
            self.stalemate_msg = "kaoš caala na bacanao*Wara Kola samaana huAa^M Ñ"
            self.resign_msg_b = "har isvakarI*kalaa iKlaaDI ijata Ñ"
            self.resign_msg_w = "har isvakarI*safod iKlaaDI ijata Ñ"
            self.draw_accept_msg = "Kola samaana huAa^M  Ñ*samaanata svaIkarI gayaIÈ"
            self.draw_reject_msg = "*AMk maola nahI KatoÈ*samaanata AsvaIkarI gayaIÈ"

            self.quit_msg = "@yaa Aap sacamaoM CaoDnaa caahto hOMÆ*Kola jatna ikyaa jaayaogaaÈ"
            self.new_game_msg = "@yaa Aap sacamaoM nayaa Kola*Sau$ krnaa caahto hOMÆ"
            self.game_saved_msg = "Kola jatna hao gayaaÈ"

            self.cont_with_friend_qn = "@yaa Aap daost ko saaqa*jaarI rKnaa caahto hOMÆ"
            self.cont_with_bot_qn = "@yaa Aap baa^T ko saaqa*jaarI rKnaa caahto hOMÆ"
            self.req_draw_qn = "@yaa Aap sacamaoM samaanata*caahto hOMÆ"
            self.resign_qn = "@yaa Aap sacamaoM har*svaIkarnaa caahto hOMÆ"
            self.quit_no_save_msg = "@yaa Aap sacamaoM Kola baMd krnaa caahto hOMÆ*Kola jatna nahI haogaa ÑÑ"
            self.new_game_qn = "@yaa Aap sacamaoM nayaa Kola*Sau$ krnaa caahto hOMÆ"

            self.switching = "*badla rha hOM"
            self.chess_bot_with = "SatrMja ka*baa^T"
            self.with_chess_bot = "*SatrMja ko baa^T ko saaqa"
            self.exclamation = ""

            self.analysis = "ivaSlaoYaNa"

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
        self.prevCLR, self.newCLR = (255, 255, 75), self.selectCLR
        self.alertFgCLR, self.alertBgCLR = (150, 150, 150), (100, 100, 100)

        self.setTheme()

        self.menuCLR, self.menuBtnCLR = self.darkCLR, self.lightCLR
        self.evalTxtBgCLR = self.lightCLR
        self.fenCLR = self.darkCLR

    def setTheme(self):
        if self.title == 'ORANGE':
            self.lightCLR = (240, 217, 181)
            self.darkCLR = (181, 136, 99)
