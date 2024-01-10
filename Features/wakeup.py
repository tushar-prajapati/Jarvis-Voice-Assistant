import pyttsx3
import speech_recognition as sr
import os
engine = pyttsx3.init('sapi5')

rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        r.energy_threshold = 300
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except Exception as e:            
            return "None"
        return query

if __name__=='__main__':
    while(True):
        query= takecommand().lower()

        if 'wake up' in query:
            speak("Initializing Jarvis")
            try:
                path="E:\\Projects\\Jarvis_Mark2\\main.py"
                os.startfile(path)
            except Exception as e:
                speak("Sorry Sir, Can you repeat?")
        elif 'wakeup' in query: 
            speak("Initializing Jarvis")
            try:
                path="E:\\Projects\\Jarvis_Mark2\\main.py"
                os.startfile(path)
            except Exception as e:
                speak("Sorry Sir, Can you repeat?")
        elif query=='jarvis':
            speak("Initializing Jarvis")
            try:
                path="E:\\Projects\\Jarvis_Mark2\\main.py"
                os.startfile(path)
            except Exception as e:
                speak("Sorry Sir, Can you repeat?")
        elif query=='hey jarvis':
            speak("Initializing Jarvis")
            try:
                path="E:\\Projects\\Jarvis_Mark2\\main.py"
                os.startfile(path)
            except Exception as e:
                speak("Sorry Sir, Can you repeat?")
        
        