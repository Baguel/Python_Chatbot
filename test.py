import speech_recognition as sr
from chatbot import detect_default_langage, translate_to_other_langage, dictionnary, text_to_voice

speech = sr.Recognizer()

def get_texte():
    langue = detect_default_langage()
    with sr.Microphone() as source:
        print(translate_to_other_langage('Parler dans le micro.....'))
        audio = speech.listen(source)
        return audio
    
def recognize_speech(audio):
    try:
        text = speech.recognize_google(audio)
        texte = dictionnary(text)
        print(f"You said: {text}")
        return texte
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")

def speech_to_text():
    while True:
        audio = get_texte()
        text = recognize_speech(audio)
        if text == "Au Revoir":
            text_to_voice(text)
            break
        else:
            print('bot: ' + text)
            text_to_voice(text)