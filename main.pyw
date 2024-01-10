
from Body.Speak import speak
from Body.Listen import Listen
import os
    
    
if __name__=="__main__":
    while(True):
        query = Listen()
        if 'wake up' in query:
                speak("Initializing Jarvis")
                try:
                    path="Jarvis.py"
                    os.startfile(path)
                except Exception as e:
                    speak("Sorry Sir, Can you repeat?")
        elif 'jarvis' == query:
                speak("Initializing Jarvis")
                try:
                    path="Jarvis.py"
                    os.startfile(path)
                except Exception as e:
                    speak("Sorry Sir, Can you repeat?")
        elif 'hey jarvis' in query:
                speak("Initializing Jarvis")
                try:
                    path="Jarvis.py"
                    os.startfile(path)
                except Exception as e:
                    speak("Sorry Sir, Can you repeat?")
        elif 'wakeup' in query:
                speak("Initializing Jarvis")
                try:
                    path="Jarvis.py"
                    os.startfile(path)
                except Exception as e:
                    speak("Sorry Sir, Can you repeat?")