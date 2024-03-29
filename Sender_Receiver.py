import socket
import threading
import time
import os

Server_socket=socket.socket()
client_socket=socket.socket()
Server_socket.bind(("",54321))
Server_socket.listen(10)
My_User= 'thirilo'
User_dictionary=dict()
def Update_Dictionary(key,value):
    User_dictionary[key]=value
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
            
def Initalise1():

    for values in User_dictionary.keys():
        try:
              f= open("User1/"+values+'.txt','r')
              f.close()
        except:
                f= open("User1/"+values+'.txt','w')
                f.close()
        


def Sent_Peroidically():
    file=open("User/NotSent.txt","r")
    f=open("User/NotSent1.txt","a+")
    while True:   
        line=file.readline()
        if not line:
            file.close()
            break
        res=line.split(":")
        ip=User_dictionary[res[0]]
        try:
          client_socket.connect((ip,54321))  
        except:
            print("Unable TO Connect")
            
            f.write(line)
        else:
            client_socket.send(res[1][:-1])
            client_socket.close()
    f.close()

def Handle_client(Conn):

    User_name=Conn.recv(1024).decode()
   # file_User=open("User_list.txt")
    print(User_name)
    Type_msg=Conn.recv(1024).decode()
    print(Type_msg)
    if Type_msg=='Message':
        Msg=Conn.recv(1024).decode()
        print("message-->",Msg)
        file=open("User/"+User_name+'.txt',"a+")
        file.write(Msg+"\n")
        print("Msg writeen")
        #Helper TO Render on Screen
        file.close()
        Conn.close()
    elif Type_msg=="File":
        Name_file=Conn.recv(1024).decode()
        list1= Name_file.split("/")
        Name_file=list1[-1]
        cwd=os.getcwd()
        file=open("User1/"+User_name+'.txt',"a+")
        file.write("1"+cwd+"/Receiver/"+Name_file+"\n")
        file.close()
        if Name_file.endswith(".txt") :
          text_file=open("Receiver/"+Name_file,"w+")
          
          while True:
              msg=Conn.recv(1024).decode()
              if not msg:
                  Conn.close()
                  text_file.close()
                  break
              text_file.write(msg)
        else:
            Other_file=open("Receiver/"+Name_file,"wb")     
            while True:
                msg=Conn.recv(1024)
                if not msg:
                    Conn.close()
                    Other_file.close()
                    break
                Other_file.write(msg)


    

def Receive():
 while True:
    Conn,addr=Server_socket.accept()
    thread1=threading.Thread(target=Handle_client,args=(Conn,))
    thread1.start()

def Sending(User,Type,msg,File_Name):
   global flag
   flag=0
   print("mama")
   global User_dictionary
   if User not in User_dictionary:
       #print(User)
       Initalise()
       flag=1
   else :
       flag=1
   print("mama")       
   if flag ==1:
       
        
       if Type =='Message':
           try:
                
                if User in User_dictionary.keys():
                    print("before Connection")
                    client_socket=socket.socket()
                    client_socket.connect((User_dictionary[User],54321))
                    print(" connection succesfullly")
                    
                else:
                    print("User is not in User Dictionary")

           except: 
                print("cannot connect")
                notsend=open("User/NotSent.txt","+a")
                notsend.write(User+":"+msg+"\n")
                notsend.close()
           else:
                client_socket.send(My_User.encode())
                client_socket.send(Type.encode())
                time.sleep(1)
                client_socket.send(msg.encode())
                client_socket.close()
       elif Type=="File":
            
            print("file--.",File_Name)
            try:
                client_socket=socket.socket()
                client_socket.connect((User_dictionary[User],54321))
                print("succesfull")
            except:
                print("Not Sent File")
            else:
                client_socket.send(My_User.encode())
                time.sleep(1)
                client_socket.send(Type.encode())
                time.sleep(1)
                client_socket.send(File_Name.encode())
                if(File_Name.endswith('.txt')):
                    file=open(File_Name,"r")
                    while True:
                        msg=file.readline()
                        if not msg:
                            file.close()
                            client_socket.close()
                            break
                        client_socket.send(msg.encode()) 
                else:
                        file=open(File_Name,"rb")
                        while True:
                            msg=file.readline()
                            if not msg:
                                file.close()
                                client_socket.close()
                                break
                            client_socket.send(msg)


Initalise()
Initalise1()