from numpy import timedelta64
from Aclu import AcluAssistant
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
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import *
from kivy.clock import Clock

import Aclu


# loading components kv file
# from components import command_btns
# from kivy.lang import Builder
Config.set('graphics', 'resizable', True)
# Builder.load_file('components/command_btns.kv')


# getting instance of aclu
aclu = AcluAssistant()


# from Aclu.features.study_mode import StudyMode


# Global Variables
# windowWidth = 1360
# windowHeight = 700
windowWidth = 900
windowHeight = 600
acluFaceWidth = aclueFaceHeight = 190
Window.size = (windowWidth, windowHeight)


class Aclu(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        self.speakAclu("Hello sir, I am ready")
        
        
    def changeFaceAclu(self, *args):
        self.ids.aclu_face.source = "Aclu/images/AcluFace1.png"        
        
    def speakAclu(self, *args):
        language = 'en'
        myobj = gTTS(text=args[0], lang=language, slow=False)
        myobj.save("audio.mp3")
        audio = MP3("audio.mp3")
        time = audio.info.length
        self.ids.aclu_face.source = "Aclu/images/AcluFace.png"
        Thread(target=os.system, args=("mpg321 audio.mp3",)).start()
        Clock.schedule_once(self.changeFaceAclu, time+1)
       
    
    def launchToolkit(self):
        self.speakAclu("Launching toolkit.")
        aclu.launchToolkit()
        self.speakAclu("Toolkit launched, sir.")
        return

    def updateDomain(self):
        self.speakAclu("Updating domain.")
        msg = aclu.updateDomain()
        self.speakAclu(msg)
        return 
    
    def studyMode(self):
        aclu.studyMode();
        return;
    
    # def test(self):
    #     # msg = aclu.testing()
    #     self.speakAclu("Hello sir what is your name, My name is Aclu sir")
        
    
        
         



class AcluAssistant(App):
    afw = NumericProperty(acluFaceWidth)
    afh = NumericProperty(aclueFaceHeight)
    ww = NumericProperty(windowWidth)
    wh = NumericProperty(windowHeight)
    buttonWidth = NumericProperty(.2)
    buttonHeight = NumericProperty(.11)
        

    def build(self):
        self.icon = "Aclu/images/icon.png"
        parent = Widget()
        parent.add_widget(Aclu())
        return parent


if __name__ == "__main__":
    AcluAssistant().run()
