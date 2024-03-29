import tkinter as tk
from Gui_chat import *
from Gui_file import *
from Gui_Video_client import Gui_Video
global temp
def Common(index,window):
    global temp
    window.destroy()
    if index==0:
        temp=Gui_chat()
    elif index==1:
        temp=Gui_file()
    else:
        temp=Gui_Video()

    
  


class GUIall():
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("600x450")
        self.window.columnconfigure(0,weight=1)
        self.window.columnconfigure(1,weight=1)
        self.window.columnconfigure(2,weight=1)
        self.window.rowconfigure(0,weight=1)
        self.window.config(bg="Purple")
        B1=tk.Button(self.window,text="Chatting app",font=("TimesNewRoman",20,"bold","italic"),anchor="center",padx=10,pady=20,bg='green',command=lambda:Common(0,self.window))
        B1.grid(row=0,column=0)
        B2=tk.Button(self.window,text="file Sharing",font=("TimesNewRoman",20,"bold","italic"),anchor="center",padx=10,pady=20,bg='green',command=lambda:Common(1,self.window))
        B2.grid(row=0,column=1)
        B3=tk.Button(self.window,text="Video conference",font=("TimesNewRoman",20,"bold","italic"),anchor="center",padx=10,pady=20,bg='green',command=lambda:Common(2,self.window))
        B3.grid(row=0,column=2)
        #B4=tk.Button(self.window,text='Add User',font=("TimesNewRoman",20,"bold","italic"),anchor="center",padx=10,pady=20,bg='green',command=lambda:AddUser(self.window))
        #B4.grid(row=1,column=0)
        Entry1=tk.Entry(self.window)
        Entry1.grid(row=2,column=0)
        Entry2=tk.Entry(self.window)
        Entry2.grid(row=2,column=1)
        self.window.mainloop()

