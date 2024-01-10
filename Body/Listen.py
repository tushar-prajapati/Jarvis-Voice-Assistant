import speech_recognition as sr
from translate import Translator

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        r.energy_threshold = 300
        audio = r.listen(source,0,10)
        # audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language= "en-in")
    except:
        return ""
    query = str(query.lower())
    return query



def Translation(text):
    line = str(text)
    translate = Translator(to_lang="English")
    result = translate.translate(line)
    # data = result.text
    print(f"You said: {result}.")
    return result

def mic_execute():
    try:
        query = Listen()
        data = Translation(query)
        return data
    except:
        print('error')

