from tkinter import  *
import threading
from Sender_Receiver import *
from tkinter import filedialog
import os
import webbrowser

# Specify the name of the subdirectory and the file you want to open
subdirectory = "User"  # Replace with your subdirectory name
file_name = "User_list.txt"  # Replace with your file name

# Create the full file path by joining the current directory with the subdirectory and file name
file_path = os.path.join(subdirectory, file_name)
global Multicasts
def select_file1(window,e1):
        file_path = filedialog.askopenfilename(title="Select a File")
        if file_path:
           
           e1.insert(0,file_path)
def Multicast_helper(e1,right_frame):
    for User in Multicasts:
        if User !="others":
            msg=e1.get()
            try:
             Sending(User,"File",0,msg)
            except:
              print('Sending the Message is Unsuccesfull')
              pass
            finally:
                f=open("User1/"+User+".txt","a+")
                f.write("0"+msg+"\n")
                f.close()
                chat_click(User,right_frame)

def Broadcast(e1,right_frame):
    for User in User_dictionary:
        if User !="others":
            msg=e1.get()
            try:
             Sending(User,"File",0,msg)
            except:
              print('Sending the Message is Unsuccesfull')
              pass
            finally:
                f=open("User1/"+User+".txt","a+")
                f.write("0"+msg+"\n")
                f.close()
                chat_click(User,right_frame)
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


def callback(event):
    webbrowser.open_new(event.widget.cget("text"))



def send_msg(User,e,right_frame):
     msg=e.get()
     e.delete(0,END)
     #print(msg+'vkregk')
     file_name=''
     try:
         Sending(User,"File",0,msg)
     except:
        print('Sending the Message is Unsuccesfull')
        pass
     finally:
        f=open("User1/"+User+".txt","a+")
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
        select=Button(right_frame,text="Select",command=lambda:select_file1(right_frame,e1))
        select.pack(side="bottom")
    else:
        file=open("User1/"+text+".txt",'r')
        print('check')
        while True:
            str=file.readline()
            print(str)
            if str=='':
                file.close()
                break
            res=str[0]
            
            if res=='0':
                l1=  Label(right_frame,text=str[1:-1],cursor='hand2',borderwidth=5,relief='raised')
                l1.pack(anchor='w')
                l1.bind("<Button-1>", callback)
            else :
                l2=  Label(right_frame,text=str[1:-1],cursor='hand2',borderwidth=5,relief='raised')
                l2.pack(anchor='e')
                l2.bind("<Button-1>", callback)
        
        e1=Entry(right_frame,text="",)
        select=Button(right_frame,text="Select",command=lambda:select_file1(right_frame,e1))
        send=Button(right_frame,text='send',command=lambda:send_msg(text,e1,right_frame),padx=20)
        select.pack(side="bottom")
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
class Gui_file() :
    
    def __init__(self):
        self.window=Tk()
        self.window.title("File App")
        self.window.geometry("600x450")
        
        self.window.rowconfigure(0,weight=1)
        self.window.columnconfigure(0,weight=1)
        self.window.columnconfigure(1,weight=3)
        left_frame=Frame(self.window,bg='green')
        right_frame=Frame(self.window,bg='#317773')
        left_frame.grid(row=0,column=0,sticky='nsew')
        right_frame.grid(row=0,column=1,sticky='nsew')
        Put_UserChat(left_frame,right_frame)

    
        

        self.window.mainloop()
       

b=Gui_file()