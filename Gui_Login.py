from tkinter import *
from Gui_all import *

try:
   f= open("User/User_Name.txt","r")
except:
  
  f1= open("User/User_Name.txt","w")
  f1.close()
else:
   f.close()
def Button_press(e1,e2,window):
   User_name=e1.get()
   Passcode=e2.get()
   e1.delete(0,END)
   e2.delete(0,END)

   try:
        f= open("User/User_Name.txt","r")
   except:
        f1= open("User/User_Name.txt","w")
        f1.close()
   else:
         f.close()
   finally:
       f= open("User/User_Name.txt","r")
       res=f.readline()

       if not res:
           f.close()
           f= open("User/User_Name.txt","w")
           f.write(User_name+" "+Passcode)
       else:
           res=res.split()
           User=res[0]
           Pass=res[1]
           #print(Pass[:-1])
           if User_name==User and Pass ==Passcode:
               print("Correct Passcode")
               window.destroy()
               temp=GUIall ()

               
           
       
   
class GUI_Login():
   def __init__(self):
      self.window=Tk()
      self.window.title("Login Page")
      self.window.geometry("400x450")
      self.window.config(bg="pink")
      self.window.columnconfigure(0,weight=1)
      self.window.columnconfigure(1,weight=2)   
      self.window.rowconfigure(0,weight=1)
      self.window.rowconfigure(1,weight=1)
      self.window.rowconfigure(2,weight=2)
      l1=Label(self.window,text="UserName",padx=20,pady=15,anchor='center')
      l1.grid(row=0,column=0)
      l2=Label(self.window,text="Passcode",padx=20,pady=10)
      l2.grid(row=1,column=0)
      
      e1=Entry(self.window,text="")
      e1.grid(row=0,column=1,sticky="ew",padx=10,)
      e2=Entry(self.window,text="")
      e2.grid(row=1,column=1,sticky="ew",padx=10,)

      submit=Button(self.window,text="Submit",command=lambda:Button_press(e1,e2,self.window))
      submit.grid(row=2,column=0)
      self.window.mainloop()
g=GUI_Login()