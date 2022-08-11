from ast import main
from server_func import build_socket
from server_func import accept_con
from server_func import connect_sockets
from server_func import send_commands



def main():
    build_socket()
    connect_sockets()
    accept_con()
    
    
main()
    