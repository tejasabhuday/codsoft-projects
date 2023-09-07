import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listen= sr.Recognizer() 
engine= pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk (text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening')
            voice=listen.listen(source)
            command=listen.recognize_google(voice)
            print(command)
    except:
        pass
    return command
    

def run_tejasAI():
    command= take_command()
    print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('do you know who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache and i would not be able to tell you the date')
    elif 'are you single' in command:
        talk('I am in a relationship with tejas the great')
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'sport' in command:
        talk("My favourite sport is football")
    elif 'who created you' in command:
        talk("I was created by Tejas Abhuday Pandey a 2nd year CS AI student from manipal institute of technology")
    else:
        talk('please say the command again')

while True:
    run_tejasAI()