#this program is intended to run on a remote server and connect client

import socket #this is to create socket 
import sys    #this is to pass commands in the terminal

#Fuction to create a socket and connect computers

def build_socket():
    
    try:
        global host
        global port
        global s

        host = ""
        port = 2345

        s= socket.socket()

#as sometimes socket cant be created and that reason will be mentioned here

    except socket.error as err:     
        print("socket creation erroe was:" + str(err))


def connect_sockets(): #we have to connect port and host socket
    try:
        global host
        global port
        global s

        s.bind((host,port)) #this function connects the host and port with socket
        s.listen(6) #this function checks the connection and tolerates 6 bad connections




    except socket.error as msg:
        print("Error in binding host and port with socket was: "+str(msg),"\n","Reconnecting...")
        connect_sockets()


    

