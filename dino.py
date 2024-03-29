"""from tkinter import *
from PIL import ImageTk, Image
import cv2
def video_stream1():
    _, frame = cap.read()
    frame=cv2.resize(frame,(200,300))
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain1.imgtk = imgtk
    lmain1.configure(image=imgtk)
    lmain1.after(1, video_stream1) 
def  video_stream2():
    _, frame = cap.read()
    frame=cv2.resize(frame,(200,300))
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain2.imgtk = imgtk
    lmain2.configure(image=imgtk)
    lmain2.after(1, video_stream2) 
def video_stream3():
    _, frame = cap.read()
    frame=cv2.resize(frame,(200,300))
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain3.imgtk = imgtk
    lmain3.configure(image=imgtk)
    lmain3.after(1, video_stream3) 
def  video_stream4():
    _, frame = cap.read()
    frame=cv2.resize(frame,(200,300))
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain4.imgtk = imgtk
    lmain4.configure(image=imgtk)
    lmain4.after(1, video_stream4) 

root = Tk()
root.geometry("800x1000")
# Create a frame
app = Frame(root, bg="white")
app.grid()
# Create a label in the frame
app.rowconfigure(0,weight=1)
app.rowconfigure(1,weight=1)
app.columnconfigure(0,weight=1)
app.columnconfigure(1,weight=1)
lmain1 = Label(app)
lmain1.grid(row=0,column=0)
lmain2 = Label(app)
lmain2.grid(row=0,column=1)
lmain3 = Label(app)
lmain3.grid(row=1,column=0)
lmain4 = Label(app)
lmain4.grid(row=1,column=1)

# Capture from camera
cap = cv2.VideoCapture(0)

# function for video streaming

video_stream1()
video_stream2()




root.mainloop()
"""
import os
print(os.getcwd())
