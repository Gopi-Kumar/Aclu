from threading import Thread
import time,os
from mutagen.mp3 import MP3
from gtts import gTTS

from kivy.core.window import Window
from kivy.config import Config

# Kivy pakagees
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import *
from kivy.clock import Clock


# loading components kv file
# from components import command_btns
from kivy.lang import Builder
Builder.load_file('components/command_btns.kv')



# getting instance of aclu
from Aclu import AcluAssistant
aclu = AcluAssistant()
Config.set('graphics', 'resizable', True)


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
        time.sleep(sec)
        self.ids.aclu_face.source = "Aclu/images/AcluFace1.png"
        
        
    def speak(self, *arg):
        self.ids.aclu_face.source = "Aclu/images/AcluFace.png"
        language = 'en'
        myobj = gTTS(text=arg[0], lang=language, slow=False)
        myobj.save("audio.mp3")
        Thread(target=os.system, args=("mpg321 audio.mp3",)).start()
        Thread(target=self.changeSource).start()
        
       
        
    

class AcluAssistant(App):
    afw = NumericProperty(acluFaceWidth)
    afh = NumericProperty(aclueFaceHeight)
    ww = NumericProperty(windowWidth)
    wh = NumericProperty(windowHeight)
    def build(self):
        self.icon = "Aclu/images/icon.png"
        parent = Widget()
        parent.add_widget(Background())
        return parent

    def testing():
        print("Testing")
 

if __name__ == "__main__":
    AcluAssistant().run()   
