import locale
from googletrans import Translator
from chatbot import main_loop
from test import get_texte, recognize_speech, speech_to_text

def detect_default_langage():
    lang = locale.getdefaultlocale()[0].split('_')[0]
    return lang

def translate_to_other_langage(texte):
    langage = detect_default_langage()
    return Translator().translate(texte, dest=langage).text

def bot():
    li = ["Dicutez avec notre Superbot alimenter avec Gemini", "Choisissez l'option 1 pour discuter avec la voix", "Choisissez l'option 2 pour discuter avec les écrits"]

    for i in range (0, len(li)): 
        print(translate_to_other_langage(li[i]))

    Choix = input(translate_to_other_langage("Fait ton choix pour continuer:") + " ")
    if Choix == '1':
        speech_to_text()
    elif Choix == '2':
        main_loop()

bot()