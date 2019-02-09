import socket

class Client(object):
    def __init__(this):
        print("Client created")
        this.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        this.addr = ""
        this.port = 0
    def connect(this, addr, port):
        this.addr = addr
        this.port = port
        this.socket.connect((addr,port))
    def send(this, stuff):
        this.socket.send(stuff)
    def exit(this):
        this.socket.send(("exit\n").encode())
        print(this.recv(64))
        this.socket.close()
        print("Client exited")
    def recv(this, length):
        return (this.socket.recv(length)).decode()

