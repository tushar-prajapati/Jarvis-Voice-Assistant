import pyttsx3
import time

def speak(text):

    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 180)
    print(f"Jarvis: {text}.")
    engine.say(text)
    engine.runAndWait()

