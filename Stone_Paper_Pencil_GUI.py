import tkinter as tk 
import random
root=tk.Tk()
root.config(background='#735c11')
root.geometry('670x450')
root.resizable(0,0)
root.title('Bharti Game')
def click(event):
    possible_options=['Rock','Paper','Scissors']
    computer= random.choice(possible_options)
    user_input= event.widget.cget('text')
    user_select.set(user_input)
    computer_select.set(computer)
    if computer==user_input:
        screen.set('Match Draw')
        result.update()
        
    elif (user_input=='Rock' and computer=='Scissors') or (user_input=='Paper' and computer=='Rock') or (user_input=='Scissors' and computer=='Paper'):
        screen.set('Congrats You Win')
        result.update()
        
    else:
        screen.set('You Loose')
        result.update()

frame=tk.Frame(root,bg='pink')
frame.pack(expand=1,fill='both',padx=30)
tk.Label(frame,text='WELCOME TO THE GAME',font='arial 15 bold',bg='#735c11',fg='white').pack(side='top',pady=1)
btn =['Rock','Paper','Scissors']
for i in btn:
    bttn=tk.Button(frame,text=i,bg='#037eab',fg='white',padx=5,pady=5,font='bold')
    bttn.pack(side='left',padx=(80,1),pady=(1,25))
    bttn.bind('<Button-1>',click)
#secon frame
frame=tk.Frame(root,bg='#d49bb9')
frame.pack(expand=1,fill='both',padx=30)
user_select=tk.StringVar()
computer_select=tk.StringVar()
tk.Label(frame,text='User Selected : ',bg='#d49bb9',font='arial 14 bold').pack(side='left',padx=(50,1))
tk.Label(frame,textvariable=user_select,bg='#d49bb9',fg='red',font='arial 12 bold').pack(side='left',padx=5)
tk.Label(frame,text='Computer Selected : ',bg='#d49bb9',font='arial 14 bold').pack(side='left',padx=(50,1))
tk.Label(frame,textvariable=computer_select,bg='#d49bb9',fg='red',font='arial 12 bold').pack(side='left',padx=5)

frame=tk.Frame(root,bg='#cc8989')
frame.pack(expand=1,fill='both',padx=30)
screen=tk.StringVar()
screen.set('')
result=tk.Label(frame,textvariable=screen,bg='#cc8989',fg='white',font='arial 25 bold')
result.pack(side='left',padx=(180,1))
root.mainloop()
