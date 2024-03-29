from tkinter import  *
import threading
from Sender_Receiver import *
import os
import time

# Specify the name of the subdirectory and the file you want to open
subdirectory = "User"  # Replace with your subdirectory name
file_name = "User_list.txt"  # Replace with your file name

# Create the full file path by joining the current directory with the subdirectory and file name
file_path = os.path.join(subdirectory, file_name)
User_last_chat=''
global Multicasts
def Multicast_helper(e1,right_frame):
    for User in Multicasts:
        if User !="others":
            msg=e1.get()
            try:
                 Sending(User,"Message","1"+msg,0)
            except:
              print('Sending the Message is Unsuccesfull')
            finally:
                f=open("User/"+User+".txt","a+")
                f.write("0"+msg+"\n")
                f.close()
                chat_click("others",right_frame)
def Broadcast(e1,right_frame):
    for User in User_dictionary:
        if User !="others":
            msg=e1.get()
            try:
                 Sending(User,"Message","1"+msg,0)
            except:
              print('Sending the Message is Unsuccesfull')
            finally:
                f=open("User/others"+".txt","a+")
                f.write("0"+msg+"\n")
                f.close()
                chat_click("others",right_frame)
def Multicast(e1,right_frame):
    root = Tk()
    root.title("choice")
    def get_selected_items():
       
       indices= listbox.curselection()
       global Multicasts
       selected_items = [listbox.get(idx) for idx in indices]
       Multicasts=selected_items
       print(f"Selected Items: {selected_items}")
       Multicast_helper(e1,right_frame)
# Create a Listbox
    listbox = Listbox(root, selectmode=MULTIPLE)  # Allow multiple selections
    listbox.pack(pady=10)

# Insert items into the Listbox
    items = [ values for values in User_dictionary.keys() if values!="others"]

    for item in items:
        listbox.insert(END, item)
    
    select_button = Button(root, text="Send", command=lambda:get_selected_items())
    select_button.pack(pady=10)

    
def Update_Peroidcally(right_frame):
    while True:
        time.sleep(10)
        if User_last_chat :
            chat_click(User_last_chat,right_frame)



def send_msg(User,e,right_frame):
     msg=e.get()
     #print(msg+'vkregk')
     global User_last_chat
     User_last_chat=User
     try:
         Sending(User,"Message","1"+msg,0)
     except:
        print('Sending the Message is Unsuccesfull')
       
     finally:
        f=open("User/"+User+".txt","a+")
        f.write("0"+msg+"\n")
        f.close()
        chat_click(User,right_frame)
       
def chat_click(text,right_frame):
    print(text)
    for widget in right_frame.winfo_children():
        widget.destroy()
    if text=="others":
        
        
        e1=Entry(right_frame,text="",)
       
        
        e1.pack(side="bottom",fill='x')
        Button(right_frame,text="Multicast",command=lambda:Multicast(e1,right_frame)).pack(anchor='e')
        Button(right_frame,text="Broadcast",command=lambda:Broadcast(e1,right_frame)).pack(anchor='w')
    else:
        file=open("User/"+text+".txt",'r')
        print('check')
        while True:
            str=file.readline()
            print(str)
            if str=='':
                file.close()
                break
            res=str[0]
            
            if res=='0':
                l1=  Label(right_frame,text=str[1:-1],borderwidth=5,relief='raised')
                l1.pack(anchor='w')
            else :
                l2=  Label(right_frame,text=str[1:-1],borderwidth=5,relief='raised')
                l2.pack(anchor='e')
        e1=Entry(right_frame,text="",)
        send=Button(right_frame,text='send',command=lambda:send_msg(text,e1,right_frame),padx=20)
        send.pack(side="bottom")
        
        e1.pack(side="bottom",fill='x')
def Put_UserChat(left_frame,right_frame):
        file_path = os.path.join(subdirectory, file_name)
        file=open("User/User_list.txt","r")
        left_frame.columnconfigure(0,weight=1)
        count=0
        while True:
             str=file.readline()
             res=str.split()
             if res == []:
                  break
             b1=Button(left_frame,text=res[0],font=("TimesNewRoman",20,"bold","italic"),bg="#00539C",fg= "#EEA47F",command=lambda t=res[0]:chat_click(t,right_frame))
             b1.grid(row=count,column=0,sticky='ew')
             count+=1


t1=threading.Thread(target=Receive,args=())
t1.start()

class Gui_chat() :
    
    def __init__(self):
        self.window=Tk()
        self.window.title("Chat App")
        self.window.geometry("600x450")
        
        self.window.rowconfigure(0,weight=1)
        self.window.columnconfigure(0,weight=1)
        self.window.columnconfigure(1,weight=3)
        left_frame=Frame(self.window,bg='green')
        right_frame=Frame(self.window,bg='#317773')
        left_frame.grid(row=0,column=0,sticky='nsew')
        right_frame.grid(row=0,column=1,sticky='nsew')
        Put_UserChat(left_frame,right_frame)
       # thread1=threading.Thread(target=Update_Peroidcally,args=(right_frame,))
       # thread1.start()+

    
        

        self.window.mainloop()
       

b=Gui_chat()
