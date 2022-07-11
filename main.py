from kivy.core.window import Window
from kivy.config import Config

# Kivy pakagees
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import *
from kivy.clock import Clock


# loading components kv file

from kivy.lang import Builder
Builder.load_file('components/command_btns.kv')



# getting instance of aclu
from Aclu import AcluAssistant
aclu = AcluAssistant()
Config.set('graphics', 'resizable', True)


# Global Variables
windowWidth = 1360
windowHeight = 700
# windowWidth = 700
# windowHeight = 600
acluFaceWidth = aclueFaceHeight = 190
Window.size = (windowWidth, windowHeight)




class Background(Widget):
    def __init__(self, **kwargs):
        super(Background, self).__init__(**kwargs)
    

    # def animateAcluFace(self, arg):
    #     if arg:
    #         self.ids.aclu_face.source = "Aclu/images/AcluFace.png"
    #     else:
    #         self.ids.aclu_face.source = "Aclu/images/AcluFace1.png"
    #     print(arg)

    # def pnt(self, *args):
    #     print("dflkj")

    # def speak(self, *arg):
    #     self.ids.aclu_face.source = "Aclu/images/AcluFace.png"
    #     Clock.schedule_once(self.pnt,2)
    #     self.ids.aclu_face.source = "Aclu/images/AcluFace.png"
        # self.animateAcluFace(1)
        # Clock.schedule_once(sel)
        # # aclu.tts(*arg)
        # self.animateAcluFace(0)
    


        
       
    
  
        




class AcluAssistant(App):
    afw = NumericProperty(acluFaceWidth)
    afh = NumericProperty(aclueFaceHeight)
    ww = NumericProperty(windowWidth)
    wh = NumericProperty(windowHeight)
    def build(self):
        self.icon = "Aclu/images/icon.png"
        return Background()
 

if __name__ == "__main__":
    AcluAssistant().run()   
