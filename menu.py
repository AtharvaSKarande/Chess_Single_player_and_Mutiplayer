import pygame
import time

from Game.values.colors import CHESS_WHITE, CHESS_BLACK
from Game.values.dimens import WIDTH, HEIGHT

GLOBAL_PATH = ""
gameFont = "Assets/product_sans_regular.ttf"
IMG_PATH = "menu_images//"
running = True
CHANGE_ACTIVITY = False

class Strings:
    str_hindi = "Hindi"
    str_english = "English"
    str_play_against = "Play Against"
    str_chess_type = "Chess Type"
    str_chess_type_sc = "Standard Chess"
    str_chess_type_nc = "No Castle"
    str_chess_type_c960 = "Chess 960"
    str_first_players_name = "First Player's Name"
    str_second_players_name = "Second Player's Name"
    str_difficulty = "Difficulty"
    str_difficulty_easy = "Easy"
    str_difficulty_medium = "Medium"
    str_difficulty_hard = "Hard"
    str_ai_color = "AI color"
    str_ai_color_black = "Black"
    str_ai_color_white = "White"
    str_settings = "Settings"
    str_play_the_game = "Play the game"
    str_continue_last_game = "Continue last game"
    str_themes = "Themes"
    str_themes_orange = "Orange"
    str_themes_classic = "Classic"
    str_info = "info"
    str_info_content = '''          There are six types of chess pieces. They are the pawn, the knight, the bishop,the rook, the queen, and the king. Pawns move up the board one square unless it's the first time they're moving when they may move two squares. Note that they cannot move backward.The pawn captures pieces one square diagonally and is the only chess piece that captures differently than the way it moves. It is also the only piece that can capture using the special en passant rule.The knight moves two squares horizontally and one vertically, or two squares vertically and one horizontally. The way the knight moves resembles the upper-case "L." The bishop can move any number of squares diagonally.The rook can move any number of squares vertically or horizontally.The queen is the most powerful piece on the board.It can move diagonally, horizontally, or vertically as many squares as it wants (unless another piece blocks it).The king can move one square in every direction.Also, the king can make use of the special castling rule together with a rook. 
              You can choose to play against another human or against the built in AI/ bot. If you select AI, difficulty of the bot, and color of the bot's pieces can also be selected. Langaugge of the interface can be selected. All these options are provided in the main menu.In settings menu you can set volume of the game and theme of the game window. You can also access settings in game window. You can choose to play against AI at any point in time in the game if you are already playing against human. You can replay previous move or move forward from previous moves. All these options are provided in main game window. At the end of the game you can evaluate your moves. You can see the moves played on the right side of the game window. Best moves and suggestions are shown at top right corner.'''

    def __init__(self, lang):

        if lang == "English":
            Strings.str_hindi = "Hindi"
            Strings.str_english = "English"
            Strings.str_play_against = "Play Against"
            Strings.str_chess_type = "Chess Type"
            Strings.str_chess_type_sc = "Standard Chess"
            Strings.str_chess_type_nc = "No Castle"
            Strings.str_chess_type_c960 = "Chess 960"
            Strings.str_first_players_name = "First Player's Name"
            Strings.str_second_players_name = "Second Player's Name"
            Strings.str_difficulty = "Difficulty"
            Strings.str_difficulty_easy = "Easy"
            Strings.str_difficulty_medium = "Medium"
            Strings.str_difficulty_hard = "Hard"
            Strings.str_ai_color = "AI color"
            Strings.str_ai_color_black = "Black"
            Strings.str_ai_color_white = "White"
            Strings.str_settings = "Settings"
            Strings.str_play_the_game = "Play the game"
            Strings.str_continue_last_game = "Continue last game"
            Strings.str_themes = "Themes"
            Strings.str_themes_orange = "Orange"
            Strings.str_themes_classic = "Classic"
            Strings.str_info = "info"
            Strings.str_info_content = '''          There are six types of chess pieces. They are the pawn, the knight, the bishop,the rook, the queen, and the king. Pawns move up the board one square unless it's the first time they're moving when they may move two squares. Note that they cannot move backward.The pawn captures pieces one square diagonally and is the only chess piece that captures differently than the way it moves. It is also the only piece that can capture using the special en passant rule.The knight moves two squares horizontally and one vertically, or two squares vertically and one horizontally. The way the knight moves resembles the upper-case "L." The bishop can move any number of squares diagonally.The rook can move any number of squares vertically or horizontally.The queen is the most powerful piece on the board.It can move diagonally, horizontally, or vertically as many squares as it wants (unless another piece blocks it).The king can move one square in every direction.Also, the king can make use of the special castling rule together with a rook. 
          You can choose to play against another human or against the built in AI/ bot. If you select AI, difficulty of the bot, and color of the bot's pieces can also be selected. Langaugge of the interface can be selected. All these options are provided in the main menu.In settings menu you can set volume of the game and theme of the game window. You can also access settings in game window. You can choose to play against AI at any point in time in the game if you are already playing against human. You can replay previous move or move forward from previous moves. All these options are provided in main game window. At the end of the game you can evaluate your moves. You can see the moves played on the right side of the game window. Best moves and suggestions are shown at top right corner.'''

        elif lang == "Hindi":
            self.font = "Assets/Shiv02.ttf"
            self.fontBold = "Assets/Shiv02.ttf"
            self.hindi_font = pygame.font.Font(self.font, 32)
            # translator = Translator()
            Strings.str_hindi = "ihndI"
            # Strings.str_hindi = translator.translate('Hindi', src='en', dest='hi')
            Strings.str_english = "AMga`ojaI"
            Strings.str_play_against = "ko iva$Qa Kolao"
            Strings.str_chess_type = "SatrMja ka p`kar"
            Strings.str_chess_type_sc = "maanak SatrMja"
            Strings.str_chess_type_nc = "ibanaa ka^sala"
            Strings.str_chess_type_c960 = "SatrMja 960"
            Strings.str_first_players_name = "phlao iKlaaDI ka naama"
            Strings.str_second_players_name = "dusaro iKlaaDI ka naama"
            Strings.str_difficulty = "kiznaaš"
            Strings.str_difficulty_easy = "Aasaana"
            Strings.str_difficulty_medium = "maQyama"
            Strings.str_difficulty_hard = "kizna"
            Strings.str_ai_color = "eAaš ka rMga"
            Strings.str_ai_color_black = "kalaa"
            Strings.str_ai_color_white = "safod"
            Strings.str_settings = "samaayaaojana"
            Strings.str_play_the_game = "Kola Kolao"
            Strings.str_continue_last_game = "ipClaa Kola Kolao"
            Strings.str_themes = "ivaYaya"
            Strings.str_themes_orange = "naarMgaI"
            Strings.str_themes_classic = "@laaisak"
            Strings.str_info = "jaanakarI"
            Strings.str_info_content = '''          Kola mao 6 p`kar ko maaohro haoto hOM. vah Pyaada rajaa ranaI }^MT haqaI GaaoDa ko naama sao jaanao jaato hOM. Pyaada 1 caala calata hO laoikna phlaI baar ihlanao pr 2 caala BaI cala sa@ta hO. Qyaana doM ik vao ipcCo kI Aaor nahI jaa sa@to.maaohra itrCo 1 vaga- ko maaohro kao Ka sa@ta hOM AaOr SatrMja ka ekmaa~ maaohra hO jaao Apnao calanao ko ZMga sao Alaga calata hO. vah ekmaa~ esaa maaohra hO jaao ek ivaSaoYa caala ena pasaoMT Kola sa@ta hOM. GaaoDa Zaš kdma kI caala Kolata hO. }^MT itrCo idSao mao iksaI BaI saM#yaa mao caala cala sa@ta hOM. haqaI iksaI BaI saM#yaa maO ]pr inacao Aqavaa dae baae cala sa@ta hOM. ranaI Kola kI sabsao takdvar maaohra haotI hOM. vao ]pr inacao dae baae Aqavaa itrCI iksaI BaI saM#yaa mao cala sa@tI hOM. rajaa iksaI BaI idSaa mao ek caala cala sa@ta hOM. rajaa haqaI kI madd sao ek ivaSaoYa caala ka^sala cala sa@ta hO.
          Aap caaho tao Kola mao maaOjaud eAaš ka AanaMd lao sa@to hOM. Saaqa hI eAaš kI kiznaaš AaOr ]saka rMga BaI caunaa jaa sa@ta hOM. Kola kI BaaYaa caunaI jaa sa@tI hOM. samaayaaojana mao Kola ka Aavaaja badlaa jaa sa@to hOM AaOr iqama BaI saoT ik jaa sai@t hOM. Agar Aap [nasaana ko saaqa Kola rho hao tao Kola ko daorana iksaI BaI samaya pr eAa[- ko saaqa Kola jaarI rK sa@to hOM. Aap ipClaI caala kao ifr sao Kola sa@to hO yaa ipClaI caala sao Aagao BaI baZ sa@to hOM. Kola Ktma haonao pr Aap Apnao Kola ka ivaSalaoYana doK sa@to hO. Kolao ga[- caalao da[- AaOr doKI jaa sa@tI hOM. savaao-%tma caalao AaOr sauJaava da[- trf ]pr idKa[- jaatI hOM.'''


# noinspection PyUnboundLocalVariable,PyArgumentList
class info_dialogue:
    def __init__(self, screen, pos, dimensions, color, color_title, title, dia_type):
        self.screen = screen
        self.pos = pos
        self.dim = dimensions
        self.color = color
        self.color_title = color_title
        self.close_img = pygame.image.load(IMG_PATH + "a.png")
        self.close_img_rect = self.close_img.get_rect(center=(self.pos[0] + self.dim[0] + 15, self.pos[1] + 55))
        self.close_img = pygame.transform.scale(self.close_img, (40, 40))
        self.title = title
        self.font = pygame.font.Font(Menu.product_sans_path, 25)
        self.text_surf = Menu.font.render(self.title, True, (253, 246, 227))
        self.text_rect = self.text_surf.get_rect(center=(self.pos[0] + 750, self.pos[1] + 20))
        self.dia_type = dia_type
        self.mute_img = pygame.image.load(IMG_PATH + "mute.png")
        self.mute_img = pygame.transform.scale(self.mute_img, (50, 50))
        self.mute_img_rect = self.mute_img.get_rect(center=(self.pos[0] + self.dim[0] + -130, self.pos[1] + 140))

        self.volume_down_img = pygame.image.load(IMG_PATH + "volume-down.png")
        self.volume_down_img = pygame.transform.scale(self.volume_down_img, (50, 50))
        self.volume_down_img_rect = self.volume_down_img.get_rect(
            center=(self.pos[0] + self.dim[0] - 130, self.pos[1] + 80))

        self.volume_up_img = pygame.image.load(IMG_PATH + "volume-up.png")
        self.volume_up_img = pygame.transform.scale(self.volume_up_img, (50, 50))
        self.volume_up_img_rect = self.volume_up_img.get_rect(center=(self.pos[0] + 130, self.pos[1] + 80))

    def rects(self):
        pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.dim[0], self.dim[1] - 25),
                         border_top_left_radius=5, border_top_right_radius=5,
                         border_bottom_left_radius=5, border_bottom_right_radius=5)

        pygame.draw.rect(self.screen, '#B3E5FC',
                         (self.pos[0] + 10, self.pos[1] + 45, self.dim[0] - 20, self.dim[1] - 80),
                         border_top_left_radius=5, border_top_right_radius=5,
                         border_bottom_left_radius=5, border_bottom_right_radius=5)
        # (253, 246, 227)

    def draw(self):
        if Menu.info_clicked:
            self.rects()
            self.screen.blit(self.text_surf, self.text_rect)
            self.screen.blit(self.close_img, self.close_img_rect)
            self.display_info()
        self.check_click()

    def display_info(self):
        string = Menu.s.str_info_content
        x, y = self.pos[0] + 15, self.pos[1] + 50
        words = [word.split(' ') for word in string.splitlines()]
        space = self.font.size(' ')[0]  # width of space
        max_width, max_height = self.dim
        for line in words:
            for word in line:
                word_surface = Menu.ui_font.render(word, True, (70, 70, 70))
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = self.pos[0] + 15  # reset x
                    y += word_height  # start on new row.
                self.screen.blit(word_surface, (x, y))
                x += word_width + space
            x = self.pos[0] + 15  # reset x
            y += word_height  # start on new row.

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.close_img_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                time.sleep(0.3)
                if self.dia_type == 'info':
                    Menu.info_clicked = False


# noinspection PyArgumentList
class DialogueBox:
    def __init__(self, screen, pos, dimensions, color, color_title, title, dia_type, volume):
        self.screen = screen
        self.pos = pos
        self.dim = dimensions
        self.color = color
        self.color_title = color_title
        self.close_img = pygame.image.load(IMG_PATH + "a.png")
        self.close_img_rect = self.close_img.get_rect(center=(self.pos[0] + self.dim[0] + 15, self.pos[1] + 55))
        self.close_img = pygame.transform.scale(self.close_img, (40, 40))
        self.title = title
        self.font = pygame.font.Font(Menu.product_sans_path, 25)
        self.text_surf = Menu.ui_font.render(self.title, True, (253, 246, 227))
        self.text_rect = self.text_surf.get_rect(center=(self.pos[0] + 190, self.pos[1] + 20))
        self.dia_type = dia_type
        self.mute_img = pygame.image.load(IMG_PATH + "mute.png")
        self.mute_img = pygame.transform.scale(self.mute_img, (50, 50))
        self.mute_img_rect = self.mute_img.get_rect(center=(self.pos[0] + self.dim[0] + -200, self.pos[1] + 140))
        self.mute_pressed = False

        self.volume_down_img = pygame.image.load(IMG_PATH + "volume-down.png")
        self.volume_down_img = pygame.transform.scale(self.volume_down_img, (50, 50))
        self.volume_down_img_rect = self.volume_down_img.get_rect(
            center=(self.pos[0] + self.dim[0] - 130, self.pos[1] + 80))
        self.down_pressed = False

        self.volume_up_img = pygame.image.load(IMG_PATH + "volume-up.png")
        self.volume_up_img = pygame.transform.scale(self.volume_up_img, (50, 50))
        self.volume_up_img_rect = self.volume_up_img.get_rect(center=(self.pos[0] + 130, self.pos[1] + 80))
        self.up_pressed = False
        self.volume = volume

        self.theme_selector = settings_Selector(self.screen, (self.pos[0] + self.dim[0] + -275, self.pos[1] + 180),
                                                (860, 500), (420, 500), Menu.s.str_themes,
                                                [Menu.s.str_themes_classic, Menu.s.str_themes_orange])

    def rects(self):
        pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.dim[0], self.dim[1] - 145),
                         border_top_left_radius=5, border_top_right_radius=5,
                         border_bottom_left_radius=5, border_bottom_right_radius=5)

        pygame.draw.rect(self.screen, (253, 246, 227),
                         (self.pos[0] + 10, self.pos[1] + 45, self.dim[0] - 20, self.dim[1] - 200),
                         border_top_left_radius=5, border_top_right_radius=5,
                         border_bottom_left_radius=5, border_bottom_right_radius=5)

    def draw(self):
        if Menu.settings_clicked:
            self.rects()
            self.screen.blit(self.text_surf, self.text_rect)
            self.screen.blit(self.close_img, self.close_img_rect)
            self.screen.blit(self.volume_up_img, self.volume_up_img_rect)
            volume_txt = self.font.render(str(Menu.volume), True, (70, 70, 70))
            self.screen.blit(volume_txt, volume_txt.get_rect(center=(self.pos[0] + 195, self.pos[1] + 80)))
            self.screen.blit(self.volume_down_img, self.volume_down_img_rect)
            self.screen.blit(self.mute_img, self.mute_img_rect)
            self.theme_selector.draw()

        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.close_img_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                time.sleep(0.3)
                if self.dia_type == 'settings':
                    Menu.settings_clicked = False
        if self.volume_up_img_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.up_pressed = True
            else:
                if self.up_pressed:
                    if Menu.volume < 100:
                        Menu.volume += 1
                    self.up_pressed = False
        if self.volume_down_img_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.down_pressed = True
            else:
                if self.down_pressed:
                    if Menu.volume > 0:
                        Menu.volume -= 1
                    self.down_pressed = False
        if self.mute_img_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.mute_pressed = True
            else:
                if self.mute_pressed:
                    Menu.volume = 0
                    self.mute_pressed = False


class Edittext:
    def __init__(self, window, x, y, default, H=50, W=50, margin_left=0, margin_right=0, margin_top=0, margin_bottom=0,
                 text_size=38, text_color=(70, 70, 70), padding=10, topLeftradius=5, bottomLeftradius=5,
                 topRightradius=5, bottomRightradius=5, borderColor=(70, 70, 70), borderFill=1,
                 font=gameFont,
                 focusColor=(150, 200, 100), background_color=(253, 246, 227), title="DUMMY", title_pos=(500, 500)):
        self.x = x
        self.y = y
        self.H = H
        self.W = W
        self.ML = margin_left
        self.MR = margin_right
        self.MT = margin_top
        self.MB = margin_bottom
        self.TLR = topLeftradius
        self.TRR = topRightradius
        self.BLR = bottomLeftradius
        self.BRR = bottomRightradius
        self.title = title
        self.title_pos = title_pos
        self.text_size = text_size
        self.text_color = text_color
        self.P = padding
        self.borderColor = borderColor
        self.bgcolor = background_color
        self.borderfill = borderFill
        self.text = default
        self.default = default
        self.window = window
        self.font = font
        self.font = pygame.font.Font(self.font, self.text_size)
        self.focusedColor = focusColor
        self.text_box = self.font.render("H", True, self.text_color)
        self.letterSize = self.text_box.get_rect().width
        self.left = 0

        self.isGreater = False
        self.focus = False

    def draw(self):
        if not self.focus:
            bCol = self.borderColor
        else:
            bCol = self.focusedColor

        text_surf = Menu.font.render(self.title, True, (253, 246, 227))
        self.window.blit(text_surf, (self.title_pos[0], self.title_pos[1]))
        # Draw the outer rect here
        pygame.draw.rect(self.window, bCol, (self.x, self.y, self.W, self.H), self.borderfill,
                         border_top_left_radius=self.TLR, border_top_right_radius=self.TRR,
                         border_bottom_left_radius=self.BLR, border_bottom_right_radius=self.BRR)

        # Draw the inner background
        pygame.draw.rect(self.window, self.bgcolor, (
            self.x + self.borderfill, self.y + self.borderfill, self.W - 2 * self.borderfill,
            self.H - 2 * self.borderfill),
                         0, border_top_left_radius=self.TLR - 3, border_top_right_radius=self.TRR - 3,
                         border_bottom_left_radius=self.BLR - 3, border_bottom_right_radius=self.BRR - 3)

        # format the contents here

        if (len(self.text)) * self.letterSize > self.W and not self.isGreater:
            self.left += 1
            self.isGreater = True

        if len(self.text) * self.letterSize < self.W:
            self.left = 0
            self.isGreater = False

        # Draw the contents here
        text = self.font.render(self.text[self.left:self.left + self.W // self.letterSize].capitalize(), True,
                                self.text_color)
        textRect = text.get_rect()
        textRect.center = (self.x + self.W / 2, self.y + self.H / 2)
        self.window.blit(text, textRect)

        # pygame.display.update()

    def eventHandler(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 1):
            if self.x < event.pos[0] < self.x + self.W:
                if self.y < event.pos[1] < self.y + self.H:
                    self.focus = True
                else:
                    self.focus = False
            else:
                self.focus = False

        if event.type == pygame.KEYDOWN:
            # print(event.key)
            if 97 <= event.key <= 122 and self.focus:
                self.text += chr(event.key)

                self.left += 1

            # Handle backspace here
            elif event.key == 8 and self.focus:
                # self.text = self.text[:-1]
                if len(self.text) != 0:
                    self.text = self.text[:-1]
                if self.left != 0:
                    self.left -= 1

            # handle the enter event
            elif event.key == 13 and self.focus:
                pass

            # handle the left key event
            elif event.key == 1073741904 and self.focus:

                if self.left != 0:
                    self.left -= 1

            # handle the right key event
            elif event.key == 1073741903 and self.focus:

                if self.left + self.W // self.letterSize != len(self.text):
                    self.left += 1
            # handle the space event here
            elif event.key == 32 and self.focus:
                self.text += " "

        # self.draw()

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text


# noinspection PyArgumentList
class Button:

    def __init__(self, screen, text, width, height, pos, elevation, Type, font):
        self.gui_font = pygame.font.Font(None, 30)
        self.screen = screen
        self.type = Type
        self.isContinue = False
        # core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#01579B'  # '#475f77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#BFC0C2'  # '#354B5E'

        # text
        self.text_surf = font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(self.screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(self.screen, self.top_color, self.top_rect, border_radius=12)
        self.screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#36AF57'  # '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True

            else:
                global CHANGE_ACTIVITY
                if self.pressed:
                    if self.type == "play-new-game" and not Menu.info_clicked:
                        CHANGE_ACTIVITY = 1

                    if self.type == "continue-last-game" and not Menu.info_clicked:
                        CHANGE_ACTIVITY = 2

                    self.dynamic_elevation = self.elevation
                    self.pressed = False
                    if self.type == "settings" and not Menu.info_clicked:
                        if Menu.settings_clicked:
                            Menu.settings_clicked = False
                        else:
                            Menu.settings_clicked = True
                    if self.type == "info":
                        if Menu.info_clicked:
                            Menu.info_clicked = False
                        else:
                            Menu.info_clicked = True
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#D74B4B'  # '#36AF57'


class ImageOption:
    # cc is caption
    def __init__(self, screen, img1, img2, x, y, length, width, cc1, cc2, decision_title, text_rect, image_rect1,
                 image_rect2):
        self.img1 = img1
        self.img2 = img2
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.cc1 = cc1
        self.cc2 = cc2
        self.decision_title = decision_title
        self.screen = screen
        self.text_rect = text_rect
        self.image_rect1 = image_rect1
        self.image_rect2 = image_rect2

    def draw(self):
        self.screen.blit(self.img1, self.image_rect1)
        self.screen.blit(self.decision_title, self.text_rect)
        self.screen.blit(self.img2, self.image_rect2)


# noinspection PyArgumentList
class settings_Selector:

    # options is list of options
    def __init__(self, screen, title_pos, options_center, next_btn_pos, selector_title, options):
        self.options = options
        self.i = 0  # option no. zero is selected by default
        self.n = len(options)
        self.path = Menu().path
        self.font = pygame.font.Font(gameFont, 30)
        self.screen = screen
        self.options_pos = options_center
        self.option_selected = options[0]
        self.left_pressed = False
        self.right_pressed = False
        self.selector_title = selector_title
        self.next_btn_pos = next_btn_pos
        self.title_pos = title_pos
        self.text_surf = Menu.ui_font.render(self.selector_title, True, (70, 70, 70))
        self.prev_img = pygame.image.load(IMG_PATH + "left-arrow.png")
        self.next_img = pygame.image.load(IMG_PATH + "right-arrow.png")
        self.prev_img = pygame.transform.scale(self.prev_img, (30, 30))
        self.next_img = pygame.transform.scale(self.next_img, (30, 30))
        self.title_width = self.text_surf.get_rect().width
        self.prev_rect = self.prev_img.get_rect(
            center=(self.title_pos[0], self.title_pos[1] + 60))
        self.next_rect = self.next_img.get_rect(center=(self.title_pos[0] + 150, self.title_pos[1] + 60))

    def draw(self):
        self.screen.blit(self.text_surf, (self.title_pos[0], self.title_pos[1]))
        self.screen.blit(self.prev_img, self.prev_rect)
        option = Menu.ui_font.render(self.options[self.i], True, (70, 70, 70))
        # self.screen.blit(option, option.get_rect(center=(970, 325)))
        # self.screen.blit(option, option.get_rect(center=(self.options_pos[0], self.options_pos[1])))
        self.screen.blit(option, option.get_rect(center=(self.title_pos[0] + 75, self.title_pos[1] + 60)))
        self.screen.blit(self.next_img, self.next_rect)
        # pygame.display.update()
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.prev_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.left_pressed = True
            else:
                if self.left_pressed:
                    self.i = (self.i - 1) % (len(self.options))
                    self.option_selected = self.options[self.i]
                    self.left_pressed = False
                    Menu.theme_selected = self.option_selected
        if self.next_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.right_pressed = True
            else:
                if self.right_pressed:
                    self.i = (self.i + 1) % (len(self.options))
                    self.option_selected = self.options[self.i]
                    self.right_pressed = False
                    Menu.theme_selected = self.option_selected


# noinspection PyArgumentList
class Selector:

    # options is list of options
    def __init__(self, screen, title_pos, options_center, next_btn_pos, selector_title, options):
        self.options = options
        self.i = 0  # option no. zero is selected by default
        self.n = len(options)
        self.path = Menu().path
        self.font = pygame.font.Font(gameFont, 40)
        self.screen = screen
        self.options_pos = options_center
        self.option_selected = options[0]
        self.left_pressed = False
        self.right_pressed = False
        self.selector_title = selector_title
        self.next_btn_pos = next_btn_pos
        self.title_pos = title_pos
        self.text_surf = Menu.font.render(self.selector_title, True, (253, 246, 227))
        self.prev_img = pygame.image.load(IMG_PATH + "left-arrow.png")
        self.next_img = pygame.image.load(IMG_PATH + "right-arrow.png")
        self.prev_img = pygame.transform.scale(self.prev_img, (50, 50))
        self.next_img = pygame.transform.scale(self.next_img, (50, 50))
        self.title_width = self.text_surf.get_rect().width
        self.prev_rect = self.prev_img.get_rect(
            center=(self.title_pos[0] + self.title_width + 40, self.title_pos[1] + 27))
        self.next_rect = self.next_img.get_rect(center=(self.title_pos[0] + next_btn_pos[0], next_btn_pos[1]))
        # selector title

        # self.text_rect = self.text_surf.get_rect(center=center)

    def draw(self):
        self.screen.blit(self.text_surf, (self.title_pos[0], self.title_pos[1]))
        self.screen.blit(self.prev_img, self.prev_rect)
        option = Menu.font.render(self.options[self.i], True, (253, 246, 227))
        # self.screen.blit(option, option.get_rect(center=(970, 325)))
        self.screen.blit(option, option.get_rect(center=(self.options_pos[0], self.options_pos[1])))
        self.screen.blit(self.next_img, self.next_rect)
        # pygame.display.update()
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.prev_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.left_pressed = True
            else:
                if self.left_pressed:
                    self.i = (self.i - 1) % (len(self.options))
                    self.option_selected = self.options[self.i]
                    self.left_pressed = False
        if self.next_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.right_pressed = True
            else:
                if self.right_pressed:
                    self.i = (self.i + 1) % (len(self.options))
                    self.option_selected = self.options[self.i]
                    self.right_pressed = False


def get_mouse_pos():
    mouse = pygame.mouse.get_pos()
    return mouse


class Menu:
    s = Strings("English")
    ui_font = pygame.font.Font(None, 30)
    font = pygame.font.Font(gameFont, 40)

    path = 'D://Python-Projects//pygame_menus//'
    product_sans_path = gameFont
    continue_last_game = False
    settings_clicked = False
    info_clicked = False
    volume = 50
    theme_selected = 'Classic'

    # Variables to be called by main game window------------------------------------------------------------------------
    var_chess_type = "Standard Chess"  # possible options - "Standard Chess", "Chess 960", "No Castle"
    var_play_against = "computer"  # possible options - "computer", "human"
    p1_name = "Ronald"
    p2_name = "Harry"
    var_theme_selected = theme_selected  # possible options - "Classic", "Blue", "Red"
    var_volume = volume
    var_is_continue_last_game = continue_last_game
    var_ai_color = "Black"  # possible options - "White", "Black"
    var_ai_difficulty = "Easy"  # possible options - "Easy", "Medium", "Hard"
    var_ui_language = "eng"  # possible options - "eng", "hindi"

    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pygame.display.set_caption('Chess: Single player and Multiplayer')
        # resolution of the screen
        self.res = self.screen.get_size()

        # white color
        self.color = (255, 255, 255)

        # light shade of the button
        self.color_light = (170, 170, 170)

        # dark shade of the button
        self.color_dark = (100, 100, 100)

        # stores the width of the
        # screen into a variable
        self.width = self.screen.get_width()

        # stores the height of the
        # screen into a variable
        self.height = self.screen.get_height()

        # project folder path
        self.path = GLOBAL_PATH
        # product-sans font path
        self.product_sans_path = gameFont

        # defining a font
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.font = pygame.font.Font(gameFont, 40)
        self.caption_font = pygame.font.Font(gameFont, 30)

        # rendering a text written in
        # this font
        self.text = self.smallfont.render('Quit', True, self.color)
        self.title_bar_name = self.font.render("Main Menu", True, self.color)

        # quit image
        self.quit_image = pygame.image.load(IMG_PATH + "a.png")
        self.quit_image = pygame.transform.scale(self.quit_image, (40, 40))

        # minimize image
        self.min_image = pygame.image.load(IMG_PATH + "b.png")
        self.min_image = pygame.transform.scale(self.min_image, (32, 32))

        # title image
        self.title = pygame.image.load(IMG_PATH + "bi2.png")
        self.title = pygame.transform.scale(self.title, (500, 175))

        # chess type images
        self.std_chess_img = pygame.image.load(IMG_PATH + "standard_chess.png")
        self.std_chess_img = pygame.transform.scale(self.std_chess_img, (80, 70))
        self.chess_960_img = pygame.image.load(IMG_PATH + "chess_960.jpg")
        self.chess_960_img = pygame.transform.scale(self.chess_960_img, (80, 70))

        self.play_against = "computer"
        self.event = None

        # play against images
        self.play_against_human_img = pygame.image.load(IMG_PATH + "human.png")
        self.play_against_human_img = pygame.transform.scale(self.play_against_human_img, (75, 75))
        self.play_against_computer_img = pygame.image.load(IMG_PATH + "ai.png")
        self.play_against_computer_img = pygame.transform.scale(self.play_against_computer_img, (75, 75))

        # language images
        self.hindi_lang_img = pygame.image.load(IMG_PATH + "india.png")
        self.hindi_lang_img = pygame.transform.scale(self.hindi_lang_img, (50, 50))
        self.english_lang_img = pygame.image.load(IMG_PATH + "united-states-of-america.png")
        self.english_lang_img = pygame.transform.scale(self.english_lang_img, (50, 50))
        self.ui_lang = "eng"

        self.clock = pygame.time.Clock()
        self.fps = 60

    # to quit menu screen
    def quit_menu(self):
        mouse = get_mouse_pos()
        if self.width - 40 <= mouse[0] <= self.width and -5 <= mouse[1] <= 40:
            self.screen.blit(self.quit_image, (self.width - 39, -3))
            self.title_bar_btn_animation()
            global running
            running = False

    # to minimize menu screen
    def min_menu(self):
        mouse = get_mouse_pos()
        if self.width - 65 <= mouse[0] <= self.width - 39 and 0 <= mouse[1] <= 32:
            self.screen.blit(self.min_image, (self.width - 64, 2))
            self.title_bar_btn_animation()
            pygame.display.iconify()

    def load_background(self):
        image = pygame.image.load(IMG_PATH + "image.png")
        image = pygame.transform.scale(image, self.res)
        return image

    def draw_title_bar(self):
        pygame.draw.rect(self.screen, (70, 70, 70), (0, 0, self.width, 30))
        pygame.draw.rect(self.screen, (70, 70, 70), (0, 0, 200, 55))
        pygame.draw.polygon(surface=self.screen, color=(70, 70, 70), points=[(200, 0), (200, 54), (250, 0)])
        self.screen.blit(self.title_bar_name, (10, 2))
        self.screen.blit(self.quit_image, (self.width - 40, -5))
        self.screen.blit(self.min_image, (self.width - 65, 0))

    def draw_bg(self):
        image = self.load_background()
        self.screen.blit(image, (0, 0))
        self.draw_title_bar()
        # self.screen.blit(self.title, (self.width / 2 - 225, 20))
        img_rect = self.title.get_rect(center=(self.width / 2, 100))
        self.screen.blit(self.title, img_rect)

    def title_bar_btn_animation(self):
        pygame.display.update()
        time.sleep(0.2)
        self.draw_title_bar()
        pygame.display.update()
        time.sleep(0.3)

    # noinspection PyUnboundLocalVariable
    def main(self):
        # player1_name = Input(self.screen, self.width*4/10 - self.width*1/150, self.width*2.7/20)
        # player2_name = Input(self.screen, 600, 225)
        button1 = Button(self.screen, Menu.s.str_play_the_game, 220, 60, (self.width / 2 - 95, self.height - 150), 4,
                         "play-new-game", Menu.ui_font)
        button2 = Button(self.screen, Menu.s.str_continue_last_game, 220, 60,
                         (self.width / 2 + 200, self.height - 150), 4, 'continue-last-game', Menu.ui_font)
        button3 = Button(self.screen, Menu.s.str_settings, 220, 60, (self.width / 2 - 397, self.height - 150), 4,
                         'settings', Menu.ui_font)
        chess_type_selector = Selector(self.screen, (550, 300), (970, 325), (600, 328), Menu.s.str_chess_type,
                                       [Menu.s.str_chess_type_sc, Menu.s.str_chess_type_c960, Menu.s.str_chess_type_nc])
        difficulty_selector = Selector(self.screen, (550, 475), (860, 500), (420, 500), Menu.s.str_difficulty,
                                       [Menu.s.str_difficulty_easy, Menu.s.str_difficulty_medium,
                                        Menu.s.str_difficulty_hard])

        first_player_name = Edittext(self.screen, 900, 389, 'Player1', 50, 250, borderFill=3,
                                     title=Menu.s.str_first_players_name,
                                     title_pos=(550, 390))
        second_player_name = Edittext(self.screen, 950, 475, 'Player2', 50, 250, borderFill=3,
                                      title=Menu.s.str_second_players_name,
                                      title_pos=(550, 475))

        settings_win = DialogueBox(self.screen, (28, 200), (400, 500), (70, 70, 70), (70, 70, 70), Menu.s.str_settings,
                                   dia_type='settings', volume=Menu.volume)
        btn_info = Button(self.screen, Menu.s.str_info, 110, 50, (self.width - 150, 75), 4,
                          'info', Menu.ui_font)
        info_win = info_dialogue(self.screen, (self.width - 1510, 190), (1475, 680), (70, 70, 70), (70, 70, 70),
                                 Menu.s.str_info, dia_type='info')
        ai_color_selector = Selector(self.screen, (550, 565), (830, 592), (390, 593), Menu.s.str_ai_color,
                                     [Menu.s.str_ai_color_black, Menu.s.str_ai_color_white])

        global running, CHANGE_ACTIVITY
        while running and not CHANGE_ACTIVITY:
            # noinspection PyBroadException
            try:
                for ev in pygame.event.get():
                    self.event = ev
                    if ev.type == pygame.QUIT:
                        running = False
                        break

                    # checks if a mouse is clicked
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        # if the mouse is clicked on the quit button the game is terminated
                        self.quit_menu()
                        self.min_menu()
                        x, y = get_mouse_pos()
                        if image_rect1.collidepoint(x, y):
                            self.play_against = "human"
                            Menu.var_play_against = "human"
                            # print("human")
                        if image_rect2.collidepoint(x, y):
                            self.play_against = "computer"
                            Menu.var_play_against = "computer"
                            # print("computer")

                        if hindi_img_rect.collidepoint(x, y):
                            self.ui_lang = "hindi"
                            Menu.var_ui_language = self.ui_lang
                            Menu.s = Strings("Hindi")
                            Menu.ui_font = pygame.font.Font('Assets/Shiv02.ttf', 30)
                            Menu.font = pygame.font.Font('Assets/Shiv02.ttf', 40)
                            Menu.main(self)
                            # print("hindi")
                        if english_img_rect.collidepoint(x, y):
                            self.ui_lang = "eng"
                            Menu.var_ui_language = self.ui_lang
                            Menu.s = Strings("English")
                            Menu.ui_font = pygame.font.Font(None, 30)
                            Menu.font = pygame.font.Font(gameFont, 40)
                            Menu.main(self)
                            # print("english")

                    first_player_name.eventHandler(ev)
                    if self.play_against == 'human':
                        second_player_name.eventHandler(ev)

                self.draw_bg()
                first_player_name.draw()
                if self.play_against == "human":
                    second_player_name.draw()
                if Menu.settings_clicked:
                    settings_win.draw()

                hindi_img_rect = self.hindi_lang_img.get_rect(center=(55, 90))
                self.screen.blit(self.hindi_lang_img, hindi_img_rect)
                english_img_rect = self.english_lang_img.get_rect(center=(55, 150))
                self.screen.blit(self.english_lang_img, english_img_rect)
                hindi_lang_title = self.caption_font.render("Hindi", True, (240, 240, 240))
                hindi_lang_rect = hindi_lang_title.get_rect(center=(130, 85))
                self.screen.blit(hindi_lang_title, hindi_lang_rect)
                eng_lang_title = self.caption_font.render("English", True, (240, 240, 240))
                eng_lang_rect = eng_lang_title.get_rect(center=(140, 147))
                self.screen.blit(eng_lang_title, eng_lang_rect)

                if self.ui_lang == "eng":
                    pygame.draw.rect(self.screen, (255, 255, 255), english_img_rect, 3)
                if self.ui_lang == "hindi":
                    pygame.draw.rect(self.screen, (255, 255, 255), hindi_img_rect, 3)

                decision_title = Menu.font.render(Menu.s.str_play_against, True, (253, 246, 227))
                x, y = self.width / 2, self.height / 2 - 200
                text_rect = decision_title.get_rect(center=(x, y))
                image_rect1 = self.play_against_human_img.get_rect(center=(x - 175, y))
                image_rect2 = self.play_against_computer_img.get_rect(center=(x + 175, y))
                if self.play_against == "human":
                    pygame.draw.rect(self.screen, (255, 255, 255), image_rect1, 4)
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), image_rect2, 4)
                caption1, caption2 = "Human", "Computer"
                play_against_selector = ImageOption(self.screen, self.play_against_human_img,
                                                    self.play_against_computer_img, 200,
                                                    200, 200, 200, caption1, caption2, decision_title, text_rect,
                                                    image_rect1,
                                                    image_rect2)
                play_against_selector.draw()

                button1.draw()
                button2.draw()
                btn_info.draw()

                button3.draw()
                chess_type_selector.draw()

                if self.play_against == 'computer':
                    difficulty_selector.draw()
                else:
                    pass

                if self.play_against == 'computer':
                    ai_color_selector.draw()
                else:
                    pass
                if Menu.info_clicked:
                    info_win.draw()

                Menu.var_chess_type = chess_type_selector.option_selected
                Menu.var_ai_color = ai_color_selector.option_selected
                Menu.var_ai_difficulty = difficulty_selector.option_selected

                Menu.var_first_players_name = first_player_name.getText()

                Menu.var_second_players_name = second_player_name.getText()

                pygame.display.update()
            except:
                pass

        if CHANGE_ACTIVITY:

            chess_type = 'STANDARD'
            if Menu.var_chess_type == Strings.str_chess_type_c960:
                chess_type = 'CHESS_960'
            if Menu.var_chess_type == Strings.str_chess_type_nc:
                chess_type = 'STANDARD_NON_CASTLE'

            vsAI = None  # Difficulty
            if Menu.var_ai_difficulty == Strings.str_difficulty_easy:
                vsAI = 'EASY'
            if Menu.var_ai_difficulty == Strings.str_difficulty_medium:
                vsAI = 'MEDIUM'
            if Menu.var_ai_difficulty == Strings.str_difficulty_hard:
                vsAI = 'HARD'

            p1Name = None
            if Menu.var_first_players_name.strip() != '':
                p1Name = Menu.var_first_players_name.strip().capitalize()

            p2Name = None
            if Menu.var_second_players_name.strip() != '':
                p2Name = Menu.var_second_players_name.strip().capitalize()

            theme = 'DEFAULT'
            if Menu.theme_selected == Strings.str_themes_orange:
                theme = 'ORANGE'

            volume = Menu.volume

            continueLastGame = CHANGE_ACTIVITY == 2

            if Menu.var_ai_color == Strings.str_ai_color_white:
                aiColor = CHESS_WHITE
            else:
                aiColor = CHESS_BLACK

            if Menu.var_play_against == 'human':
                vsAI = None
                aiColor = None

            language = 'ENGLISH'
            if Menu.var_ui_language == 'hindi':
                language = 'HINDI'

            return [vsAI, aiColor, theme, language, volume, chess_type, p1Name, p2Name, continueLastGame]
