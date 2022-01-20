import socket



class Server():
    def __init__(self):
        self.host = "localhost"
        self.port = 8080
        self.backlog = 10
        self.bufsize = 1024

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
    
    def c2s(self):
        print(" === sub thread === ")
        self.sock.listen(self.backlog)
        while True:
            cli, address = self.sock.accept()
            print(f"Connection from {address} has been established!")            
            mes = cli.recv(self.bufsize).decode("utf-8")
            if mes == 'q':
                print("sub thread is being terminaited")
                break
            print(mes)

        self.sock.close()

sv = Server()
sv.run()


