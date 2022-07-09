

# import speech_recognition as sr

# r = sr.Recognizer()

# while(1):
#     try:
#         with sr.Microphone() as source2:
#             r.adjust_for_ambient_noise(source2, duration=0.3)
#             # r.energy_threshold(3000)
#             print("Listenning")
#             audio2 = r.listen(source2)
#             print(audio2)
#             print("recognising")
#             MyText = r.recognize_google(audio2)

#             print("recognised")

#             MyText = MyText.lower()
#             print("Did you say "+MyText)
#             print("give me command")


#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))

#     except sr.UnknownValueError:
#         print("I am unable to hear you sir")


from gtts import gTTS
import os
mytext = 'Hello gk, aclu is here to help you'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("audio.mp3")

# Playing the converted file
os.system("mpg321 audio.mp3")
