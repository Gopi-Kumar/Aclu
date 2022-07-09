from Aclu import AcluAssistant


obj = AcluAssistant()


def speak(text):
    obj.tts(text)


speak("Hello sir, I am ready to work")

