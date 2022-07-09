
import speech_recognition as sr
from gtts import gTTS
import os

class AcluAssistant:
    def __init__(self):
       
        pass

    def listen(self):
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.energy_threshold = 4000
                audio = r.listen(source)

            try:
                print("Recognizing")
                command = r.recognize_google(audio, language='en-in').lower()
                print(f'You said:{command}')
            except:
                print('Please try again')
                command = self.listen()
            
            return command
            
        except Exception as e:
            print(e)
            return False

    def tts(self, text):
        language = 'en'
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save("audio.mp3")
        os.system("mpg321 audio.mp3")

