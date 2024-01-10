from Body.Speak import speak
from Body.Listen import Listen
import datetime
import webbrowser
import os
import time
import pyautogui
import random
import requests
from pygame import mixer
import keyboard
from Brain.AiBrain import replyBrain


#Present time
strTime= datetime.datetime.now().strftime("%H:%M")
today = datetime.date.today()#Today's date

def todayDate():
    speak(today)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour <= 16:
        speak("Good afternoon Sir")
    elif hour >= 0 and hour <= 4:
        speak(f"Sir, It's already {strTime} You should sleep now.")
    else:
        speak("Good evening Sir")
def startupMusic():
    mixer.init()
    mixer.music.load("Music\\start.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()

def shutdownMusic():
    mixer.init()
    mixer.music.load("Music\\shutdown.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play()

def ageofai():
    ageYear = int(str(today.year)) - 2022
    ageMonth = int(str(today.month)) - 10
    ageDay = int(str(today.day)) - 29
    years = 'years'
    months = 'months'
    days = 'days'
    if ageDay==1:
        days= days.replace("days", "day")        
    if ageMonth==1:
        months= months.replace("months", "month")
    if ageYear==1:
        years= years.replace("years", "years")

    speak(f"Sir, I am {ageYear} {years}. {ageMonth} {months}. And {ageDay} {days} old")

if __name__=='__main__':
    startupMusic()
    time.sleep(6)
    wishMe()
    while(True):
        query = Listen()
        query = str(query)
        print(query)
        if len(query)<=1:
            pass
        elif('date today' in query) or ('what is the date' in query):
            speak("Sir, Today's date is")
            todayDate()
        elif 'time' in query:
            speak(f"Sir, the time is {strTime}")
        elif 'open' in query:
            query = query.replace("open","")
            speak(f"Opening {query} sir")
            pyautogui.press('win')
            time.sleep(1)
            keyboard.write(query)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(0.5)
        elif 'kholo' in query:
            query = query.replace("kholo","")
            speak(f"Opening {query} sir")
            pyautogui.press('win')
            time.sleep(1)
            keyboard.write(query)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(0.5)
        elif 'ip address' in query:
            try:
                ip= requests.get("https://api.ipify.org").text
                speak(f"Sir Your i P address is {ip}")
            except Exception as e:
                speak("Sorry Sir, There's some error")
        elif ('sleep' in query) or ('so kyon nahin jaate' in query) or ('take rest' in query) or ('take a break' in query) or ('so jao' in query) or ('stop listening' in query):
            speak("Ok Sir, Tell me if you need anything.")
            speak("Just say")
            speak("Wake up Jarvis")
            shutdownMusic()
            time.sleep(2)
            exit()
        elif 'search' in query:
            query = query.replace("search", "")
            speak(f"Searching {query} on google sir")
            webbrowser.open(f"www.google.com/search?q={query}")
        else:
            try:
                result = replyBrain(query)
                speak(result)
            except:
                speak("Sorry Sir, Can You repeat?")