'''
virtual_assistant.py
A basic virtual assistant called Topaz that utilizes text to speech and microphone input.
Commands: print, play, time, who/what, thank you (exit)
GH
last update: 31/12
'''

# To start, followed: https://www.youtube.com/watch?v=AWvsXxDtEkU&list=WL&index=22&t=50s

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate',220)

run = True

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'print' in command:
                command = command.replace('print', '')
                print(command)
    except:
        pass
    return command

def command_play(command):
    vid = command.replace('play', '')
    talk('Okay. Playing' + vid)
    print('playing' + vid)
    vid = command.replace('by', '')
    pywhatkit.playonyt(vid, use_api = True)

def command_time(command):
    time = datetime.datetime.now().strftime('%I:%M %p')
    print(time)
    talk('The time right now is ' + time)

def command_whatwho(command):
    thing = command.replace('what is', '')
    thing = command.replace('who is', '')
    thing = command.replace('what are', '')
    thing = command.replace('who are', '')
    info = wikipedia.summary(thing, 1)
    print(info)
    talk(info)

def run_assistant():
    command = take_command()
    print(command)
    if 'play' in command:
        command_play(command)
    elif 'time' in command:
        command_time(command)
    elif ('who' in command) or ('what' in command):
        command_whatwho(command)
    elif 'thank you' in command:
        talk("Thank you. Goodbye.")
        return False
    else:
        talk("Please say that again.")
    return True

talk("Hello. I am Topaz. What can I do for you?")

while(run == True):
    run = run_assistant()