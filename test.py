from mutagen.mp3 import MP3
audio = MP3("audio.mp3")
print(audio.info.length)



# from kivy.app import App
# from kivy.uix.image import AsyncImage
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
# import time


# from threading import Thread
# # creating the App class


# class MyApp(App):
#     def build(self):
#         parent = Widget()
        
#         #creating and adding image to widget
#         self.img = AsyncImage(
#             source='http://kivy.org/logos/kivy-logo-black-64.png')
#         self.img.pos = (400,400)
        
#         #creating btn and adding press handler
#         self.change_img_btn = Button(text="Change Image ")
#         self.change_img_btn.bind(on_press = self.changeImageSource)
        
        
#         #adding widget to Widget instance
#         parent.add_widget(self.img)
#         parent.add_widget(self.change_img_btn)
#         return parent;

#     def changeSource(self):
#         self.ids.source = "https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a"
    
#     def waitForMe(self):    
#         time.sleep(4)
#         print("Wait end")
    
#     def changeImageSource(self,*args):
#         Thread(target=self.changeSource).start()
#         Thread(target=self.waitForMe).start()
#         print("Hello")

# # run the App
# MyApp().run()
