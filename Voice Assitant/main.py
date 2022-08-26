import datetime
from email.mime import audio
import speech_recognition as sr
import pyaudio
import pyttsx3
import os
import webbrowser
import wikipedia
from selenium import webdriver
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak(f"hello {user} i'm { ai_name}! How may i help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
       

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    #you can also take input as a string 
    speak('what do you want me to call you?')
    user = takecommand()
    while user == 'None':
        user = takecommand()
    speech_name = "jarvis"
    speak(f'hello {user} by default my name is jarvis. do you want to change it?')
    name_change_or_not = takecommand().lower
    # ask user for AI name
    while name_change_or_not != 'no' or 'None':
        speak('what do you want to name me?')
        ai_name = takecommand()
        while ai_name == 'None':
            ai_name = takecommand()
        break

    wishme()
    while True:
        query = takecommand().lower()
        # reads wikipedia upto 2 sentences
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        # open goggle crome when search is said
        elif 'search' in query:
            speak(' what do you want to search')
            search1 = takecommand().lower()
            search1 = search1.replace(' ', '+')
            browser = webdriver.Chrome('chromedriver')
            matched_element = browser.get("https://www.google.com/search?q=" +
                                          search1 + "&start=")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            print(time)
            speak(f'{user},Time is {time}')
        elif 'open code' in query:
            # enter your IDE path
            code_path = "C:\\Users\\vikas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        while 'quit' or 'kill' or 'end' or 'finish the programe' in query:
            break
