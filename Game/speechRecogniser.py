import speech_recognition as sr
from Game.values.dimens import coordinates

class SpeechRecogniser:
    def __init__(self):
        self.recogniser = sr.Recognizer()

    def getMove(self):
        try:
            with sr.Microphone() as src:
                self.recogniser.adjust_for_ambient_noise(src, duration=0.2)
                print("Listening...")
                # listens for the user's input

                audio2 = self.recogniser.listen(src)
                print("Done.")

                # Using google to recognize audio

                MyText = self.recogniser.recognize_google(audio2)

                recognisedText = MyText.lower()
                print("I heard : ", recognisedText)

                if recognisedText == "quit":
                    return "quit"
            return recogniseMove(recognisedText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return "ERROR"

        except sr.UnknownValueError:
            print("unknown error occured")
            return "ERROR"

# e4, Bc3, Raa4, Nxd4, Qexd4+, castle, e8=Q

# Raa4, Qexd4+, e8=Q

def replace(text, string, array):
    if string in text:
        idx = text.index(string)
        tmp = text[:idx]
        tmp.extend(array)
        tmp.extend(text[idx + 1:])
        return tmp
    return text

def modifyText(text):
    text = text.split(' ')

    text = replace(text, 'intex', ['e', 'takes'])
    text = replace(text, '8x', ['a', 'takes'])

    return text

def recogniseMove(text):
    text = modifyText(text)
    le = len(text)

    if text[0] == 'play':

        # Castling
        if le == 3 and text[1] in ['short', 'shot'] and text[2] == 'castle':
            return 'O-O'
        elif le == 3 and text[1] == 'long' and text[2] == 'castle':
            return 'O-O-O'

        if le == 2:
            return text[1]  # Pawn

        move = ''
        if text[1] in ['king']:
            move = 'K'  # king
        elif text[1] in ['knight', 'night']:
            move = 'N'  # knight
        elif text[1] in ['queen']:
            move = 'Q'  # Queen
        elif text[1] in ['bishop']:
            move = 'B'  # Bishop
        elif text[1] in ['rook', 'ryuk', 'ruk', 'roop']:
            move = 'R'  # Rook

        if text[1] in coordinates.values():
            if le == 3:
                return move + text[1] + text[2]
            if le == 4 and text[2] == 'takes':
                return move + text[1] + 'x' + text[3]

        elif le == 3:
            return move + text[2]

        elif text[2] in coordinates.values():
            if le == 4:
                return move + text[2] + text[3]
            if le == 5 and text[3] == 'takes':
                return move + text[2] + 'x' + text[4]

        elif le == 4 and text[2] == 'takes':
            return move + 'x' + text[3]

        elif le == 4 and text[1] == 'promote':
            if text[3] in ['queen']:
                return text[2] + '=Q'
            elif text[3] in ['rook', 'ryuk', 'ruk', 'roop']:
                return text[2] + '=R'
            elif text[3] in ['bishop']:
                return text[2] + '=B'
            elif text[3] in ['knight', 'night']:
                return text[2] + '=N'

    return "ERROR"
