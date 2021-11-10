from menu import Menu
from play import Play

if __name__ == "__main__":
    menu = Menu()
    pref = menu.main()

    playGame = Play()
    if pref is not None:
        playGame.startWithPref(pref)
