import socket
import cv2
import tkinter as tk
from tkinter import *
import threading
from PIL import ImageTk, Image
import pickle
import struct
global curr_User
curr_User=""
Video_socket=socket.socket(socket.SOCK_DGRAM)
My_user="thirilo"
Video_socket.bind(('',65432))
cap=cv2.VideoCapture(0)
Video_socket.listen(4)  
User_dictionary=dict()
def Initalise():
   User_list= open("User/User_list.txt","r")
   global flag,ip
   flag=0
   while True:
       line=User_list.readline()
       res=line.split()
       if res == [] :
           User_list.close()
           break
       else:
           User_dictionary[res[0]]=res[1]
           print(res)
           try:
              f= open("User/"+res[0]+'.txt','r')
              f.close()
           except:
                f= open("User/"+res[0]+'.txt','w')
                f.close()
Initalise()
def video_stream1(lmain,window):
 while curr_User==My_user:
    _, frame = cap.read()
    frame=cv2.resize(frame,(500,400))
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    window.update()
    #lmain.after(1, lambda:video_stream1(lmain)) 
def Handle_client(client_socket):
    vid = cv2.VideoCapture(0)
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
    while (vid.isOpened()):
            img, frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)
            
    client_socket.close() 
def VideoSender():
    while True:
        client_socket, addr = Video_socket.accept()
        thread1=threading.Thread(target=Handle_client,args=(client_socket,))
        thread1.start()
        
            
def chat_click(User,right_frame,window):
    for widget in right_frame.winfo_children():
        widget.destroy()
    global curr_User
    curr_User=User
    
    if User==My_user:
          Label1=Label(right_frame)
          Label1.grid()
          video_stream1(Label1,window)
    elif User!="others":
          Label1=Label(right_frame)
          Label1.grid()
          VideoReceiver(User,Label1,window)
          
def VideoReceiver(User,Labels,window):
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = 'localhost'
    port = 65432
    client_socket.connect((User_dictionary[User], port))
    data = b""
    payload_size = struct.calcsize("Q")
    while True:
        while len(data) < payload_size:
            packet = client_socket.recv(8 * 1024)
            if not packet: break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(8 * 1024)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)

        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        Labels.imgtk = imgtk
        if curr_User==User:
            Labels.configure(image=imgtk)
            window.update()

    client_socket.close()
def Put_UserChat(left_frame,right_frame,window):
        #file_path = os.path.join(subdirectory, file_name)
        file=open("User/User_list.txt","r")
        
        left_frame.columnconfigure(0,weight=1)
        count=1
        b1=Button(left_frame,text=My_user,font=("TimesNewRoman",20,"bold","italic"),bg="#00539C",fg= "#EEA47F",command=lambda t=My_user:chat_click(t,right_frame,window))
        b1.grid(row=0,column=0,sticky='ew')
        while True:
             str=file.readline()
             res=str.split()
             if res == []:
                  break
             if res[0]!="others":
                b1=Button(left_frame,text=res[0],font=("TimesNewRoman",20,"bold","italic"),bg="#00539C",fg= "#EEA47F",command=lambda t=res[0]:chat_click(t,right_frame,window))
                b1.grid(row=count,column=0,sticky='ew')
                count+=1
thread1=threading.Thread(target=VideoSender,args=())
thread1.start()
class Gui_Video():
     def __init__(self):
          self.window=tk.Tk()
          self.window.geometry("800x600")
          self.window.rowconfigure(0,weight=1)
          
          self.window.columnconfigure(0,weight=1)
          self.window.columnconfigure(1,weight=3)
          left_frame=Frame(self.window,bg='#00539C')
          right_frame=Frame(self.window,bg='#317773')
          left_frame.grid(row=0,column=0,sticky='nsew')
          right_frame.grid(row=0,column=1,sticky='nsew')
          Put_UserChat(left_frame,right_frame,self.window)
          self.window.mainloop()



ans=Gui_Video()