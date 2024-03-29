from gtts import gTTS
import pygame
from io import BytesIO
import google.generativeai as genai
import os
import locale
from googletrans import Translator
from chrome import web
from vision import visionpicture

# Détecte le langage de la machine
def detect_default_langage():
    lang = os.getenv('LANG')

    if lang:
        lang_code = lang.split('.')[0].split('_')[0]
        return lang_code
    else:
        return None

# Traduis dans le langage de la machine
def translate_to_other_langage(texte):
    langage = detect_default_langage()
    translator = Translator()
    return translator.translate(texte, dest=langage).text

# Lis le texte dans le langage de la machine
def text_to_voice(texte):
    langage = detect_default_langage()
    tts = gTTS(text=texte, lang=langage, slow=False)
    # Utilisation de BytesIO pour stocker l'audio en mémoire
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)

    # Initialisation de pygame
    pygame.mixer.init()
    pygame.mixer.music.load(audio_bytes)

    # Lecture de l'audio
    pygame.mixer.music.play()

    # Attente de la fin de la lecture
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def response_with_gemini(prompt):
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        }
    ]

    genai.configure(
        api_key=os.environ['google'])
    model = genai.GenerativeModel(
        model_name='gemini-pro',
        safety_settings=safety_settings
    )

    completion = model.generate_content(
    prompt,
    generation_config={
        'temperature': 0,
        'max_output_tokens': 800
    })
    return completion.text


def dictionnary(texte):
    dialogue = {
        "bonjour": "Comment vous allez?",
        "bien et toi" : "ca va bien merci de demander",
        "j'ai besoin de toi": "Demander moi ce que vous voulez ??",
        "merci beaucoup": "Tout le plaisir a été pour moi",
        "taureau" : "je suis un superbot alimenter par Gemini créer par florentin GANFON",
        "japon" : "Le Japon est un pays insulaire situé dans l'océan Pacifique. Il comporte des villes denses, des palais impériaux, des parcs nationaux montagneux ainsi que des milliers de temples et de sanctuaires."
    }
    for i, j in dialogue.items():
        s = Translator().translate(texte, dest="fr").text
        if i == s.lower():
            return translate_to_other_langage(j)
        elif translate_to_other_langage("chrome") in texte:
            return texte
        elif translate_to_other_langage("analyses") in texte:
            return texte
        
    return response_with_gemini(texte)

def main_loop():
    while True:
        texte = input(translate_to_other_langage("Entrer votre texte:") + ' ')
        text = dictionnary(texte)
        if text != " " and translate_to_other_langage("chrome") in text:
            li = text.split()
            web(li[1])
        elif text != " " and translate_to_other_langage("analyses") in texte:
            picture = input(translate_to_other_langage('entrer votre image: '))
            prompt = input(translate_to_other_langage('entrer votre promt: '))
            descript = visionpicture(prompt, picture)
            print(translate_to_other_langage(descript))
            text_to_voice(descript)
        else:
            print("Bot: " + text)
            text_to_voice(text)