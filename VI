import tkinter as tk 
from PIL import ImageTk,Image
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
from datetime import datetime
import wikipedia
from tkinter import messagebox

def speak(audio):
    engine = pyttsx3.init()
    #this is use for change the voice into male to female by default it is male voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    # through this we can set the speed of audio by default it is 200
    engine.setProperty('rate',180)
    engine.say(audio)
    engine.runAndWait()

def console_data(string):
    console_screen.delete(1.0,tk.END)
    console_screen.insert(1.0,string)
    console_screen.update()

def click(event):
    query=user_query.get()
    query=query.lower()
    if 'exit the program' in query or 'close the program' in query:
        console_data('thanks for using me,good bye')
        speak('thanks for using me,good bye')
        exit()
    elif query =='' or query ==' ' or query =='  ' or query =='   ':
        console_data('Type something')
        speak('Type something')
    elif 'hello' in query : 
        console_data('hello sir i am happy to help you')       
        speak('hello sir i am happy to help you')    
    elif 'date' in query:
        now = datetime.now()
        today_date=now.strftime("%B %d, %Y")
        console_data(today_date)
        speak(today_date)
    elif 'time' in query:
        now = datetime.now()
        time_now=now.strftime("%H:%M") 
        console_data(time_now)       
        speak(time_now)
    elif 'are you crazy' in query or 'you crazy' in query:
        console_data('yeah little bit i guess ')
        speak('yeah little bit i guess ')
    elif 'thank you' in query or 'thanks' in query:
        console_data('My pleasure sir')
        speak('My pleasure sir')
    elif 'who invented you' in query or 'invented you' in query:
        console_data('he is a genius')
        speak('he is a genius')
    elif 'play music' in query:
        console_data('opening groove music')
        speak('opening groove music')
        os.system("start mswindowsmusic:")
    elif 'weather' in query:
        console_data('opening weather')
        speak('opening weather')
        os.system('start BingWeather:')    
        ###  using os.system() funtion ###
    elif 'open notepad' in query or 'open the notepad' in query:
        console_data('opening notepad')
        speak('opening notepad')
        os.system('start notepad')
    elif 'close notepad' in query or 'close the notepad' in query:
        console_data('closeing the notepad')
        speak('closeing the notepad')
        os.system('taskkill /im notepad.exe /t /f')
    elif 'open vlc' in query or 'open the vlc' in query:
        console_data('opening vlc player')
        speak('opening vlc player')
        os.system('start vlc')
    elif 'close vlc' in query or 'close the vlc' in query:
        console_data('closeing the vlc player')
        speak('closeing the vlc player')
        os.system('taskkill /im vlc.exe /t /f')
        ### using os.startfile() function ####
    elif 'open pictures' in query or 'open images' in query:
        console_data('opening pictures folder')
        speak('opening pictures folder')
        os.startfile(r'C:\Users\HACKER\pictures')
    elif 'open documents' in query:
        console_data('opening documents folder')
        speak('opening documents folder')
        os.startfile(r'C:\Users\HACKER\documents')
    elif 'open downloads' in query:
        console_data('opening downloads folder')
        speak('opening downloads folder')
        os.startfile(r'C:\Users\HACKER\downloads')
    elif 'open music' in query:
        console_data('opening music folder')
        speak('opening music folder')
        os.startfile(r'C:\Users\HACKER\music')
    elif 'open videos' in query:
        console_data('opening videos folder')
        speak('opening videos folder')
        os.startfile(r'C:\Users\HACKER\videos')
        ### using webbrowser.open() ###
        # webbrower() funtion open the given url in the default browser
    elif 'open goole chrome' in query or 'open google' in query or 'open chrome' in query or 'open the google' in query:
        console_data('opening google')
        speak('opening google')
        webbrowser.open('www.google.com')
    elif 'close the google' in query or 'close google chrome' in query or 'close chrome' in query or 'close the google chrome' in query: 
        console_data('closeing google chrome')
        speak('closeing google chrome')
        os.system('taskkill /im chrome.exe /t /f')
    elif 'open the youtube' in query or 'open youtube' in query:
        console_data('opening youtube')
        speak('opening youtube')
        webbrowser.open('www.youtube.com')
    elif 'close youtube' in query or 'close the youtube' in query: 
        console_data('closeing youtube')
        speak('closeing youtube')
        os.system('taskkill /im chrome.exe /t /f')
    elif 'open my gmail' in query or 'open gmail' in query:
        console_data('opening gmail')
        speak('opening gmail')
        webbrowser.open('www.gmail.com')
    elif 'open my facebook' in query or 'open facebook' in query or 'open fb' in query or 'open the facebook' in query:
        console_data('opening facebook')
        speak('opening facebook')
        webbrowser.open('www.facebook.com') 
    ##### shutdonw , restart , log off the computer #####
    elif 'shut down' in query or 'shutdonw' in query :
        console_data('Youe PC will shut donw after few time')
        speak('you computer will shuting down in a few seconds')
        os.system('shutdown/s')
        # break
    elif 'restart' in query:
        console_data('Youe PC will restart after few time')
        speak('you computer will restarting in a few seconds')
        os.system('shutdown/r')
        # break
    elif 'log off' in query or 'logoff' in query:
        console_data('Youe PC will log off after few time')
        speak('you computer will log off')
        os.system('shutdown/l')
        # break
    elif 'wikipedia' in query:
        status.set('Searching...')
        status_of_speach.update()
        speak("searching from wikipedia")
        query=query.replace('wikipedia',' ')
        try :
            #wikipedia.search() gives the list of most relevant pages
            result=wikipedia.search(query)
            # in the wikipedia.summary() the sentences parameter will decide the how many lines you want
            status.set('')
            status_of_speach.update()
            console_data(wikipedia.summary(result[0],sentences=2))
            speak('according to wikipedia')
            speak(wikipedia.summary(result[0],sentences=2))
        except Exception as e:
            console_data(e)
            speak(e)
    else:
        console_data('the query that you ask to me , is not available in my database so i decide to redirect it into browser')
        speak('the query that you ask to me , is not available in my database so i decide to redirect it into browser')
        webbrowser.open(query)

def click_for_speak_input(event):
    speak('click')
    # use this infinite loop here because if user cant say anything -
    # then this function run the except part and retun nothing 
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\nListening....")
            status.set('Listening..')
            status_of_speach.update()

            speak('i am ready for your command')
            #that r.adjust_for_ambient_noise use for surronding noise
            r.adjust_for_ambient_noise(source, duration=0.5)
            #the r.listen take the audio as parameter
            audio = r.listen(source)

        try:
            status.set('Recognizing..')
            status_of_speach.update()
            print("Recognizing....")
            #that recognize.google take the audio file in first parameter and change it into text
            query = r.recognize_google(audio, language = 'Eng-In')
            print(f'User said: {query}\n')
            status.set('')
            status_of_speach.update()
            user_query.set(query)
            search_box.update()
            # call the click() for automaticaly execute the query
            click(event)
            return query
        except Exception as e :
            console_data('please say again ,may be internet issue or due to alot of noise i cant hear you sir')
            speak('please say again ,may be internet issue or due to alot of noise i cant hear you sir')
            print(e)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to exit?"):
        root.destroy()
        speak('Thank you for using me')

if __name__ == "__main__": 

    root = tk.Tk()
    root.iconbitmap('assistant_icon.png')
    root.title('Bharti Assistant')
    root.configure(bg='#AAD6FD')

    #    frame  adding image,and entry widget   
    frame=tk.Frame(root,bg='#AAD6FD')
    frame.pack()
    img_object=Image.open('Assistant_image.jpg')
    img_object=img_object.resize((920,320))
    bg_img=ImageTk.PhotoImage(img_object)
    label=tk.Label(frame,image=bg_img)
    label.pack(pady=5,padx=10)

    user_query=tk.StringVar()
    user_query.set('')
    search_box=tk.Entry(frame,textvariable=user_query,width=30,font='arial 14')
    search_box.pack(fill='x',padx=50,ipady=5)

    frame=tk.Frame(root,background='#AAD6FD')
    frame.pack(expand=1,fill='x',padx=400,pady=10,anchor='n')

    btn_img=Image.open('search.png')
    btn_img=btn_img.resize((90,40))
    btn_img=ImageTk.PhotoImage(btn_img)

    btn=tk.Button(frame,bg='white',font='arial 16 bold',image=btn_img)
    btn.bind('<Button-1>',click)
    btn.bind('<Enter>',lambda event :btn.configure(background='red'))
    btn.bind('<Leave>',lambda event :btn.configure(background='white'))
    btn.pack(pady=1,padx=20,side='left',anchor='n')

    icon_img=Image.open('microphone.png')
    icon_img=icon_img.resize((30,30))
    iconimg=ImageTk.PhotoImage(icon_img)
    icon=tk.Button(frame,image=iconimg,bg='#AAD6FD',border=0)
    icon.bind('<Button-1>',click_for_speak_input)
    icon.bind('<Enter>',lambda event :icon.configure(background='white'))
    icon.bind('<Leave>',lambda event :icon.configure(background='#AAD6FD'))
    icon.pack(ipady=5,ipadx=5,side='left',anchor='n')

    status=tk.StringVar()
    status.set('')
    status_of_speach=tk.Label(frame,textvariable=status,bg='#AAD6FD',font='arial 12 italic')
    status_of_speach.pack(side='left',pady=10,padx=12,anchor='n')

    frame=tk.Frame(root,highlightbackground="green", highlightcolor="green", highlightthickness=2)
    frame.pack(expand=1,fill='both',ipady=100,pady=10,padx=80)

    console_screen =tk.Text(frame,font='arial 14')
    console_screen.pack(expand=1,fill='both')

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
