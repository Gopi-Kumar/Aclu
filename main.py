from Aclu import AcluAssistant
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color


from kivy.core.window import Window
Window.size = (1370, 748)


class CanvasWidget(Widget):
    pass


# Aclu assitent configuratio
obj = AcluAssistant()


def speak(text):
    obj.tts(text)


class AcluAssistant(App):
    def build(self):
        return CanvasWidget()


AcluAssistant().run()
