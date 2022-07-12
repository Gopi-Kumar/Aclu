from ast import arg
import speech_recognition as sr
from gtts import gTTS
import os
import pyttsx3
from threading import Thread

from Aclu.features import update_domain, launch_mytoolkit



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
        # Thread(target=os.system, args=("mpg321 audio.mp3"))
        
    def updateDomain(self):
        self.tts("Updating domain")
        msg = update_domain.update_domain()
        self.tts(msg)
        
    def launchToolkit(self):
        self.tts("Lauching toolkit")
        launch_mytoolkit.launch_mytoolkit()
        self.tts("Toolkit launched sir")
        
        
    


