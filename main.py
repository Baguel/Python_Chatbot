import os
from googletrans import Translator
from chatbot import main_loop
from test import speech_to_text

def detect_default_langage():
    lang = os.getenv('LANG')

    if lang:
        lang_code = lang.split('.')[0].split('_')[0]
        return lang_code
    else:
        return None

def translate_to_other_langage(texte):
    langage = detect_default_langage()
    return Translator().translate(texte, dest=langage).text

def bot():
    li = ["Discutez avec notre Superbot alimenté par Gemini", "Choisissez l'option 1 pour discuter à voix haute", "Choisissez l'option 2 pour discuter par écrit", "Appuyez Ctrl + c pour mettre fin a la session"]

    for i in range (0, len(li)): 
        print(translate_to_other_langage(li[i]))
    

    Choix = input(translate_to_other_langage("Fait ton choix pour continuer:") + " ")
    if Choix == '1':
        speech_to_text()
    elif Choix == '2':
        main_loop()

bot()