import speech_recognition as sr
import pyttsx3
import os
import webbrowser
from datetime import datetime
from currencyconverter import currency_converter
from password_genrater import password_genrater

def speak(audio):
    engine = pyttsx3.init()
    #this is use for change the voice into male to female by default it is male voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    # through this we can set the speed of audio by default it is 200
    engine.setProperty('rate',180)
    engine.say(audio)
    engine.runAndWait()
def wishme():
    now = datetime.now()
    current_time = int(now.strftime("%H"))
    if current_time>=1 and current_time<12:
        print('good morning')
        speak('good morning')
    elif current_time>=12 and current_time<=15:
        print('good afternoon')
        speak('good afternoon')
    else:
        print('good evening')
        speak('good evening')

def command():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\nListening....")
            speak('i am ready for your command')
            #that r.adjust_for_ambient_noise use for surronding noise
            r.adjust_for_ambient_noise(source, duration=0.5)
            #the r.listen take the audio as input
            audio = r.listen(source)

        try:
            print("Recognizing....")
            #that recognize.google take the audio file in first parameter and change it into text
            query = r.recognize_google(audio, language = 'Eng-In')
            print(f'User said: {query}\n')
            return query
        except Exception as e :
            speak('please say again ,may be internet issue or due to alot of noise i cant hear you sir')
            print('please say again')
            print(e)

if __name__ == "__main__":

    wishme()
    speak('hello sir i am your assistant ')
    while True:
        query=command().lower()
        if 'exit the program' in query or 'close the program' in query:
            speak('thanks for using me,good bye')
            print('thanks for using me,good bye')
            exit()

        elif 'hello' in query :
            speak('hello sir i am happy to help you')
            print('hello sir i am happy to help you')
            
        elif 'date' in query:
            now = datetime.now()
            today_date=now.strftime("%B %d, %Y")
            print(today_date)
            speak(today_date)
        elif 'time' in query:
            now = datetime.now()
            time_now=now.strftime("%H:%M")
            print(time_now)
            speak(time_now)
        elif 'good morning' in query or 'good afternoon' in query or 'good evening' in query:
            wishme()
        elif 'are you crazy' in query or 'you crazy' in query:
            speak('yeah little bit i guess ')
        elif 'thank you' in query or 'thanks' in query:
            print('My pleasure sir')
            speak('My pleasure sir')
        elif 'who invented you' in query or 'invented you' in query:
            print('he is a genius')
            speak('he is a genius')
            #### using my own written scripts in python ####
        elif 'strong password' in query or 'password' in query:
            speak('enter the lenght of the password')
            pass_len=int(input('enter here : '))
            your_pass = password_genrater(pass_len)
            speak('here is your password sir : ')
            print('your password :',your_pass)
        elif 'currency converter' in query or 'currency' in query:
            speak('enter total amount here : ')
            amount = int(input('enter total amount : '))
            speak('select the country')
            covert=currency_converter(amount)
            print(covert)
            speak(covert) 
            ###  using os.system() funtion ###
        elif 'open notepad' in query or 'open the notepad' in query:
            speak('opening notepad')
            os.system('start notepad')
        elif 'close notepad' in query or 'close the notepad' in query:
            speak('closeing the notepad')
            os.system('taskkill /im notepad.exe /t /f')
        elif 'open vlc' in query or 'open the vlc' in query:
            speak('opening vlc player')
            os.system('start vlc')
        elif 'close vlc' in query or 'close the vlc' in query:
            speak('closeing the vlc player')
            os.system('taskkill /im vlc.exe /t /f')
            ### using os.startfile() function ####
        elif 'open pictures' in query or 'open image' in query:
            speak('opening pictures folder')
            os.startfile(r'C:\Users\HACKER\pictures')
        elif 'close pictures' in query or 'close image' in query or 'exit pictures' in query:
            speak('closeing pictures folder')
            os.system('taskkill /f /t /im explorer.exe && start explorer.exe')
            ### using webbrowser.open() ###
        elif 'open goole chrome' in query or 'open google' in query or 'open chrome' in query or 'open the google' in query:
            speak('opening google')
            webbrowser.open('www.google.com')
        elif 'close the google' in query or 'close google chrome' in query or 'close chrome' in query or 'close the google chrome' in query: 
            speak('closeing google chrome')
            os.system('taskkill /im chrome.exe /t /f')
        elif 'open the youtube' in query or 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('www.youtube.com')
        elif 'close youtube' in query or 'close the youtube' in query: 
            speak('closeing youtube')
            os.system('taskkill /im chrome.exe /t /f')
        elif 'open my gmail' in query or 'open gmail' in query:
            speak('opening gmail')
            webbrowser.open('www.gmail.com')
        elif 'open my facebook' in query or 'open facebook' in query or 'open fb' in query or 'open the facebook' in query:
            speak('opening facebook')
            webbrowser.open('www.facebook.com') 
        ##### shutdonw , restart , log off the computer #####
        elif 'shut down' in query or 'shutdonw' in query :
            speak('you computer will shuting down in a few seconds')
            os.system('shutdown/s')
            break
        elif 'restart' in query:
            speak('you computer will restarting in a few seconds')
            os.system('shutdown/r')
            break
        elif 'log off' in query or 'logoff' in query:
            speak('you computer will log off')
            os.system('shutdown/l')
            break
        else:
            # print('please say again..')
            speak('the query that you ask to me , is not available in my database so i decide to redirect it into browser')
            webbrowser.open(query)