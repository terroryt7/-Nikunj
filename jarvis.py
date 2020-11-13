import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
from requests import get


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
            speak("Good Afternoon!")
     
    else:
          speak("Good Evening!")

    speak ("hello sir  I am jarvis  How may I help you?") 

def takecommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source) 
     
    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e) 
        print("say that again please...")
        return"None"          
    return query
def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your gmail','your password')
    server.sendmail('your gmail',to,content)
    server.close() 

if __name__ == "__main__":
    wishme()
    while True:
    #if 1:

        query = takecommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
           speak('serching wikipedia...')
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)

        elif 'open youtube' in query:
            speak("open youtube in progress")
            webbrowser.open("youtube.com")  
        
        elif 'open google' in query:
            speak("open google in progress")
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,The time is{strTime}") 

        elif 'open chrome' in query:
            speak("open crome is in progress")
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"   
            os.startfile(codePath)

        elif 'open download' in query:
            speak("dawnlod opneing in progress")
            code = "C:\\Program Files (x86)\\Internet Download Manager\\IDMan.exe"
            os.startfile(code)  
        elif 'email to friend' in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = "friend gmail"
                sendemail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e) 
                speak("sorry i can't able to sent this email")
                
        
        elif 'what is your name' in query:
            speak("my name is jarvis")

        elif 'who are you' in query:
            speak("I am ai based robot") 

        elif 'open main drive' in query:
            speak("c drive is in progress") 
            pc = "C:\\" 
            os.startfile(pc)

        elif 'my ip' in query:
            ip = get('https://api.ipify.org').text
            print(ip) 
            speak(f"your ip is {ip}")

        elif 'search in google' in query:
            speak("what should i search?")
            cm = takecommand(). lower()
            speak("searching in progress")
            webbrowser.open(f"{cm}")

        elif 'exit' in query:
            speak("thanks for using")
            sys.exit()
        
        
            
            


