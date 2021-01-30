import tkinter as tk 
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
import os
win=tk.Tk()
win.wm_iconbitmap('notes.png')
win.geometry('1920x1080')
win.title('Untitle - Bharti notepad')

# define menu items function
file=None
def open():
    global file
    if file==None:
        # if there is not any cotent in the text editor this code will execute
        file=filedialog.askopenfile(mode='r',initialdir='C://hacker/documents/',title='select the file',filetypes=(('text files','.txt'),('all files','*.*')))
        if file==None:
             # if user just open the file dialog and dont open any file then its doesnt change any thing and return none
            return
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,file.read())
        file.close()
        # file.name function use for to get the textIOwrapper file path
        # os.path.basename() func return the name of file
        win.title(os.path.basename(file.name)+'- Bharti Notepad')
    else:
        # if there is already any cotent in the text editor this code will execute
        file=filedialog.askopenfile(mode='r',initialdir='C://hacker/documents/',title='select the file',filetypes=(('text files','.txt'),('all files','*.*')))
        if file==None:
            # if user just open the file dialog and dont open any file then its doesnt change any thing and return none
            return
        else:    
            # if user open the file dialog
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,file.read())
            file.close()
            win.title(os.path.basename(file.name)+'- Bharti Notepad')
def new():
    text_editor.delete(1.0,tk.END)
    win.title('Untitle - Bharti Notepad')
def save():
    global file
    file=filedialog.asksaveasfile(mode='w',initialdir='C://hacker/document/',title='save as',defaultextension=('.txt'))
    file.write(text_editor.get(1.0,tk.END))
    file.close()
    win.title(os.path.basename(file.name)+'- Bharti Notepad')
def exit():
    answer=messagebox.askquestion('notepad','do you want to exit')
    if answer=='yes':
        quit()
def cut():
    text_editor.event_generate(('<<Cut>>'))
def copy():
    text_editor.event_generate(('<<Copy>>'))
def paste():
    text_editor.event_generate(('<<Paste>>'))
def help():
    messagebox.showinfo('Notepad','Contact To This Email Address \"bhartu425@gamil.com\"\nFor any Enquery')

# define toolbar_frame buttons functions  
def bold():
    # the current_tag variable return the selected text tag name
    current_tag=text_editor.tag_names('sel.first')
    # 1st time else condition will run 
    # because user not define any bold or other tag here
    if 'bold' in current_tag:
        # when there already the bold tag this code will remove the bold tag
        text_editor.tag_remove('bold','sel.first','sel.last')
    else:
        # user define the bold tag here ,the first argument in the tag_add() funtion are the tag name
        # sel.fist and sel.last means here selected the text form starting to last
        text_editor.tag_add('bold','sel.first','sel.last')
        # configuring the define tag
        text_editor.tag_configure('bold',font='Consolas 11 bold')
def italic():
    current_tag =text_editor.tag_names('sel.first')
    if 'italic' in current_tag:
        text_editor.tag_remove('italic','sel.first','sel.last')
    else:    
        text_editor.tag_add('italic','sel.first','sel.last')
        text_editor.tag_config('italic',font='Consolas 11 italic')
def underline():
    current_tag=text_editor.tag_names('sel.first')
    if 'underline' in current_tag:
        text_editor.tag_remove('underline','sel.first','sel.last')
    else:    
        text_editor.tag_add('underline','sel.first','sel.last')
        text_editor.tag_config('underline',font='Consolas 11 underline')
# insert image function
def insert_image():
    file=filedialog.askopenfilename(initialdir='C://hacker/pictures/', filetypes=(('images file','.jpg'),('all files','*.*')))
    img=Image.open(file)
    # in tkinter when we add image through funtion we need to make the global variable
    global pic
    pic=ImageTk.PhotoImage(img)
    position=text_editor.index(tk.INSERT)
    # through this postion var we got that where is our cursor
    text_editor.image_create(position,image=pic)

# creating toolbar_frame
toolbar_frame=tk.Frame(win)
toolbar_frame.pack(side='top',padx=20,pady=1)
# creating scroll bar and text editor
scroll_bar=tk.Scrollbar(win)
scroll_bar.pack(side='right',fill='y')

text_editor=tk.Text(win,yscrollcommand=scroll_bar.set,font='Consolas 11',undo=True)
text_editor.pack(expand=1,fill='both')

scroll_bar.configure(command=text_editor.yview)
# creating buttons for toolbar_frame
bold_img=Image.open('bold.png')
bold_img=bold_img.resize((15,15))
bold_btn_image=ImageTk.PhotoImage(bold_img)

btn=tk.Button(toolbar_frame,command=bold,image=bold_btn_image)
btn.pack(side='left',padx=4)

italic_img=Image.open('italic.png')
italic_img=italic_img.resize((15,15))
italic_btn_image=ImageTk.PhotoImage(italic_img)

btn=tk.Button(toolbar_frame,text='italic',command=italic,image=italic_btn_image)
btn.pack(side='left',padx=4)

underline_img=Image.open('underline.png')
underline_img=underline_img.resize((15,15))
underline_btn_image=ImageTk.PhotoImage(underline_img)

btn=tk.Button(toolbar_frame,text='underline',command=underline,image=underline_btn_image)
btn.pack(side='left',padx=4)

undo_img=Image.open('undo.png')
undo_img=undo_img.resize((15,15))
undo_btn_image=ImageTk.PhotoImage(undo_img)

    # for undo and redo we dont need to define any funtion it have predefine function
btn=tk.Button(toolbar_frame,text='undo',command=text_editor.edit_undo,image=undo_btn_image)
btn.pack(side='left',padx=4)

redo_img=Image.open('redo.png')
redo_img=redo_img.resize((15,15))
redo_btn_image=ImageTk.PhotoImage(redo_img)

btn=tk.Button(toolbar_frame,text='redo',command=text_editor.edit_redo,image=redo_btn_image)
btn.pack(side='left',padx=4)

insert_img=Image.open('image.png')
insert_img=insert_img.resize((15,15))
insert_btn_image=ImageTk.PhotoImage(insert_img)

btn=tk.Button(toolbar_frame,text='insert image',command=insert_image,image=insert_btn_image)
btn.pack(side='left',padx=4)

# creating menubar
menu_bar=tk.Menu(win)

file_menu=tk.Menu(menu_bar,tearoff=0)
file_menu.add_command(label='Open',command=open)
file_menu.add_command(label='New',command=new)
file_menu.add_command(label='Save',command=save)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=exit)

menu_bar.add_cascade(label='File',menu=file_menu)

edit_menu=tk.Menu(menu_bar,tearoff=0)
edit_menu.add_command(label='Cut',command=cut)
edit_menu.add_command(label='Copy',command=copy)
edit_menu.add_command(label='Paste',command=paste)

menu_bar.add_cascade(label='Edit',menu=edit_menu)

help_menu=tk.Menu(menu_bar,tearoff=0)
help_menu.add_command(label="Help",command=help)
menu_bar.add_cascade(label='Help',menu=help_menu)

win.configure(menu=menu_bar)



win.mainloop()
