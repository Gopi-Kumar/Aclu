from threading import Thread
import time
import os
from turtle import back
from mutagen.mp3 import MP3
from gtts import gTTS

# Kivy pakagees
from kivy.core.window import Window
from kivy.config import Config
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import *
from kivy.clock import Clock

import Aclu


# loading components kv file
# from components import command_btns
# from kivy.lang import Builder
Config.set('graphics', 'resizable', True)
# Builder.load_file('components/command_btns.kv')


# getting instance of aclu
from Aclu import AcluAssistant
aclu = AcluAssistant()




# from Aclu.features.study_mode import StudyMode


# Global Variables
# windowWidth = 1360
# windowHeight = 700
windowWidth = 700
windowHeight = 600
acluFaceWidth = aclueFaceHeight = 190
Window.size = (windowWidth, windowHeight)





class Background(Widget):
    def __init__(self, **kwargs):
        super(Background, self).__init__(**kwargs)

    def changeSource(self):
        audio = MP3("audio.mp3")
        sec = audio.info.length
        time.sleep(4)
        self.ids.aclu_face.source = "Aclu/images/AcluFace1.png"

    def speak(self, *arg):
        self.ids.aclu_face.source = "Aclu/images/AcluFace.png"
        language = 'en'
        myobj = gTTS(text=arg[0], lang=language, slow=False)
        myobj.save("audio.mp3")
        Thread(target=os.system, args=("mpg321 audio.mp3",)).start()
        Thread(target=self.changeSource).start()

class CommandButtons(BoxLayout):
    # def __init__(self, **kwargs):
    #     super(CommandButtons, self).__init__(**kwargs)
        
    def launchToolkit(self):
        return

    def updateDomain(self):
        aclu.updateDomain()
        return 
    
    def studyMode(self):
        # Background.speak(Background(),"")
        # StudyMode()
        return

class AcluAssistant(App):
    afw = NumericProperty(acluFaceWidth)
    afh = NumericProperty(aclueFaceHeight)
    ww = NumericProperty(windowWidth)
    wh = NumericProperty(windowHeight)

    def build(self):
        self.icon = "Aclu/images/icon.png"
        parent = Widget()
        parent.add_widget(Background())
        parent.add_widget(CommandButtons())
        return parent


if __name__ == "__main__":
    AcluAssistant().run()
