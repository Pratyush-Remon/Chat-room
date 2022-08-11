from ast import main
from server_func import build_socket
from server_func import accept_con
from server_func import connect_sockets


if __name__=="__main__":
    def main():
        build_socket()
        connect_sockets()
        accept_con()
    
    main()
    