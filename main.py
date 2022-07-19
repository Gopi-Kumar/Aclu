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
aclu = AcluAssistant()


# from Aclu.features.study_mode import StudyMode


# Global Variables
# windowWidth = 1360
# windowHeight = 700
windowWidth = 900
windowHeight = 600
acluFaceWidth = aclueFaceHeight = 190
Window.size = (windowWidth, windowHeight)
  
class Background(Widget):
    def __init__(self, **kwargs):
        super(Background, self).__init__(**kwargs)
    
    def changeBacgrondAclu1(self):
        self.ids.aclu_face.source = "Aclu/images/AcluFace.png"
        
    
# class CommandButtons(BoxLayout):   
   

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
