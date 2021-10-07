
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
