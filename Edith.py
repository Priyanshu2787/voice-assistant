from os import terminal_size
import pyttsx3
from pyttsx3.engine import Engine
import datetime
import speech_recognition as sr
import smtplib
import webbrowser
import os
import pyautogui
import psutil

engine= pyttsx3. init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
newVoiceRate= 150
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("This is Edith")

def time():
    Time= datetime.datetime.now().strftime('%I:%M:%S')
    speak("Current Time is")
    speak(Time)

def date():
    year= int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date= int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Sir")
    hour= datetime.datetime.now().hour
    if hour>= 6 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
    elif hour>=18 and hour<=24:
        speak("good evening")
    else:
        speak("good night")

    speak("Edith at your service, how can i help you")
wishme()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold= 1
        audio= r.listen(source)
     
    try:
         print("recognizing")
         query = r.recognize_google(audio, language="en in")
         print(query)
    
    except Exception as e:
        print(e)
        speak("say that again please")
        return "NONE"
        
    return query

takecommand()

def sendmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("test@gamil.com")
    server.sendmail("test@gmail.com",to, content)
    server.close()

def screenshot():
    img= pyautogui.screenshot()


def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu usage is"+ usage)

    battery = psutil.sensors_battery
    speak("battery is at")
    speak(battery.percent )



if __name__ == "__main__":
    
    wishme()

    while True:
        query= takecommand().lower()
        print(query)

        if "time" in query:
            time()
        
        elif "date" in query:
            date()
        
        elif "offline" in query:
            quit()
        
        elif "send email" in query:
            try:
                speak("what should i say")
                content = takecommand()
                speak("to whom u want to send a email")
                to = takecommand()
                sendmail(to, content)
                speak("email was sent successfully")
            except Exception as e:
                speak(e)
                speak("unable to send")
        
        elif "search in chrome" in query:
            speak("what you want to search")
            chromepath = ""
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        
        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s/t 1")
        elif "restart" in query:
            os.system("shutdown /r/t 1")
        
        elif "play songs" in query:
            song_dir= ""
            song = os.listdir(song_dir)
            os.startfile(os.path.join(song_dir, song[0]))
        
        elif "remember that" in query:
            speak("what should i remember")
            data= takecommand()
            speak("u said me to remember"+ data)
            remember = open("data.txt", w)
            remember.write(data)
            remember.close()

        elif "screenshot" in query:
            screenshot()
            speak("done")

        elif "cpu" in query:
            cpu()
       
