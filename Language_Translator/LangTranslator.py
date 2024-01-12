import pyttsx3
import speech_recognition as sr
from googletrans import Translator
from tkinter import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 130)

def speak(audio, lang):
    if lang == 'hi':
        # Use the Hindi voice
        engine.setProperty('voice', voices[0].id)
    elif lang == 'zh':
        # Use the Chinese voice
        engine.setProperty('voice', voices[0].id)
    elif lang == 'ja':
        # Use the Japanese voice
        engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        translator = Translator()
        c = input('''Enter language in which to translate (for chinese,japanese and hindi
        voice translator is not available):
            1. French
            2. Spanish
            3. German
            4. Italian
            5. Portuguese
            6. Chinese
            7. Japanese
            8. Arabic
            9. Russian
            10. Hindi\n''')
        try:
            dest_lang = {
                '1': 'fr',
                '2': 'es',
                '3': 'de',
                '4': 'it',
                '5': 'pt',
                '6': 'zh',
                '7': 'ja',
                '8': 'ar',
                '9': 'ru',
                '10': 'hi'
            }[c]
            result = translator.translate(query, dest=dest_lang)
            with open("file1.txt", "w", encoding="utf-8") as f:
                f.write(result.text)
        except KeyError:
            print('Enter correct language')
            return

    with open('file1.txt', 'r', encoding='utf-8') as f:
        speak(f.read(), dest_lang)
        f.close()

if __name__ == '__main__':
    takeCommand()
    f = open('file1.txt', 'r', encoding='utf-8')
    root=Tk()
    root.geometry('600x600')
    root.minsize(200,100)
    root.maxsize(1000,700)
    s=f.read()
    print('Translated text: ',s)
    text=Label(text=s)
    text.pack()
    root.mainloop()
    f.close()
