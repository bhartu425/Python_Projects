import tkinter as tk 
win=tk.Tk()
win.geometry('350x350')
win.resizable(0,0)
win.title('Bhartu Calculator')
value=''
def click(event):
    btn_text=event.widget.cget('text')
    global value
    if btn_text=='=':
        # convert eval into str because it return the int value
        value=str(eval(value))
        result.set(value)
        screen.update()
    elif btn_text=='C':
        value=''
        result.set(value)
        screen.update()
    else:
        value=value+str(btn_text)
        result.set(value)
        screen.update()
# function to change properties of button on hover 
def changeOnHover(button_var):
    default_color=win.cget('bg') 
    # background on entering widget 
    button_var.bind("<Enter>", func=lambda single_arguments: button_var.config(background='#dddddd')) 
    # background color on leving widget 
    button_var.bind("<Leave>", func=lambda single_arguments: button_var.config(background=default_color)) 

frame=tk.Frame(win,background='#dddddd')
frame.pack(expand=True,fill='both')

result=tk.StringVar()
result.set('')
screen=tk.Label(frame,textvariable=result,font='24',background='#dddddd')
screen.pack(side='left',fill='both',ipadx=10)

for j in range(1,5):
    frame=tk.Frame(win,bg='white')
    frame.pack(expand=1,fill='both')
    if j==1:
        btn_values=[1,2,3,'+']
        for i in btn_values:
            buttn=tk.Button(frame,text=i,border = 0,font=25)
            buttn.bind('<Button-1>',click)
            changeOnHover(buttn)
            buttn.pack(side='left',expand=1,fill='both')
    if j==2:
        btn_values=[4,5,6,'-']
        for i in btn_values:
            buttn=tk.Button(frame,text=i,border = 0,font=25)
            buttn.bind('<Button-1>',click)
            changeOnHover(buttn)
            buttn.pack(side='left',expand=1,fill='both')
    if j==3:
        btn_values=[7,8,9,'/']
        for i in btn_values:
            buttn=tk.Button(frame,text=i,border = 0,font=25)
            buttn.bind('<Button-1>',click)
            changeOnHover(buttn)
            buttn.pack(side='left',expand=1,fill='both')
    if j==4:
        btn_values=['C',0,'=','*']
        for i in btn_values:
            buttn=tk.Button(frame,text=i,border = 0,font=25)
            buttn.bind('<Button-1>',click)
            changeOnHover(buttn)
            buttn.pack(side='left',expand=1,fill='both')        
win.mainloop()
