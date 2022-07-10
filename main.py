from Aclu import AcluAssistant
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'resizable', True)

from kivy.core.window import Window

windowWidth = 1360
windowHeight = 720

# Window.size=(windowWidth,windowHeight)
Window.size = (700, 600)

obj = AcluAssistant()

class Background(Widget):
    def __init__(self, **kwargs):
        super(Background, self).__init__(**kwargs)

    def speak(self):
        print("speaking")


# Aclu assitent configuratio





class AcluAssistant(App):
    def build(self):
        # parent = Widget()
        # self.canvasWidget = Background()
        # #Aclu Face
        # self.acu_face = Image(source='Aclu/images/AcluFace.png')
        # self.acu_face.allow_stretch = True
        # self.acu_face.keep_ratio = False
        # self.acu_face.width = 170
        # self.acu_face.height = 170
        # self.acu_face.pos = ((windowWidth-self.acu_face.width)/2, (windowHeight-self.acu_face.height)/2)

      

        # #adding widget to app
        # parent.add_widget(self.canvasWidget)
        # parent.add_widget(self.acu_face)
        # return parent;
        return Background()

if __name__ == "__main__":
    AcluAssistant().run()   
