from gtts import gTTS
import pygame
from io import BytesIO
import google.generativeai as genai
import os

def text_to_voice(texte):
    tts = gTTS(text=texte, lang='fr', slow=False)
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
    genai.configure(
        api_key=os.environ['google'])
    model = genai.GenerativeModel(
        model_name='gemini-pro'
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
        "bonjour": "bonjour Comment vous allez aujourd'hui?",
        "ca va et toi" : "ca va bien merci de demander",
        "j'ai besoin de toi": "Demander moi ce que vous voulez ??",
        "ou est le japon ??" : "État insulaire d'Asie orientale baigné au nord par la mer d'Okhotsk, à l'est et au sud par l'océan Pacifique, et à l'ouest par la mer du Japon, qui le sépare du continent asiatique, le Japon est formé de quatre îles principales (Hokkaido, Honshu, Shikoku et Kyushu)",
        "merci beaucoup": "Tout le plaisir a été pour moi",
        "hakari" : "Kinji Hakari est un élève de terminale de l'école d'exorcisme de Tokyo qui est actuellement suspendus pour s'être embrouillé avec la hiérarchie, en particulier les conservateurs. Depuis, semble-t-il, Kinji dirige le Fight Club, un endroit où s'organisent des combats entre exorcistes.",
    }
    for i, j in dialogue.items():
        if texte == i:
            return j
        
        else:
            res = response_with_gemini(texte)
            return res


def main_loop():
    while True:
        texte = input()
        text = dictionnary(texte)
        if text == "exit":
            break
        elif text == "Au Revoir":
            text_to_voice(text)
            break
        else:
            print(text)
            text_to_voice(text)

main_loop()
