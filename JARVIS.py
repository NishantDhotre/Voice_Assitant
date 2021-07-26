import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")
    
    speak("I am jarvis sir. how may i help you!")

def takeCommands():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in' )
        print(f"user said: {query} \n")

    except Exception :
        print("pleas say that again...")
        return "none"
    return query

def sendEmail(to,content):
    server =smtplib.SMTP('smnpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('dhotrenishant@gmail.com','password')
    server.sendmail('dhotrenishant@gmail.com',to,content)
    server.close()

def browes(s):
    chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    if '.com' in s:
        webbrowser.get(chromedir).open("https://"+s)
    else   : 
     webbrowser.get(chromedir).open("https://www.google.com/search?q="+s)
    





if __name__=="__main__":
    wishMe()
    while (True):
        query = takeCommands().lower()


        if 'wikipedia' in query :
            query= query.replace("wikipedia"," ")
            result=wikipedia.summary(query,sentences=1)
            speak("according wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            browes('youtube.com')

        elif 'play music' in query:
            music_dir="D:"#add the music directory path  here
            #C:\\Users\\nishant\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\spotify.exe
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))#the [0] will play the first song in list you can code it to play song whic you tels to paly

        elif 'time' in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir the time is {strTime}")

        elif 'open game' in query:
             game="C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\Uplay.exe"
             os.startfile(game)

        elif 'send mail'in query:
            try:
                speak("to whome should i send mail")
                to=takeCommands()
                speak("what should i send")
                content=takeCommands
                sendEmail(to,content)
                print("email is sent.!")
            except Exception:
                print("email is not sent ")

        elif 'search' in query:
             speak("what you want  to search")
             s=takeCommands()
             browes(s)    

        elif 'exit' in query :
             break