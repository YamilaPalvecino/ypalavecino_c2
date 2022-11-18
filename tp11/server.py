import socketserver, subprocess, socket, threading, getopt, sys

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'h:p:a:')
    if len(opt) != 3:
        print("Por favor ingrese bien la cantidad de argumentos")
        exit()
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()

for (op,ar) in opt:
    if op == '-h':
       host = str(ar)
    if op == '-p':
        port = int(ar)
    if op == '-a':
        args = str(ar)

class Thread(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class Process(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThreadIPV6(socketserver.ThreadingMixIn, socketserver.TCPServer):
    ip_type = socket.AF_INET6

class ProcessIPV6(socketserver.ForkingMixIn, socketserver.TCPServer):
    ip_type = socket.AF_INET6

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            if len(data) == 0 or data == "exit":
                print(f"Cliente desconectado {self.client_address[0]}")
                exit(0)
            command = subprocess.Popen([data], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = command.communicate()
            if command.returncode == 0:
                ans = "OK \n"+ stdout
                print(f'El comando {data.decode("ascii")} se ejecuto')
            else:
                ans = "ERROR \n"+ stderr
                print(f'El comando {data.decode("ascii")} no se ejecuto')
            self.request.send(ans.encode('ascii'))

def server(direction, port):
    if direction[0] == socket.AF_INET and args == "t":
        print("IPv4 con hilos")
        server = Thread((host,port), MyTCPHandler)
    elif direction[0] == socket.AF_INET and args == "p":
        print("IPv4 con procesos")
        server = Process((host,port), MyTCPHandler)
    elif direction[0] == socket.AF_INET6 and args == "t":
        print("IPv6 con hilos")
        server = ThreadIPV6((host,port), MyTCPHandler)
    elif direction[0] == socket.AF_INET6 and args == "p":
        print("IPv6 con procesos")
        server = ProcessIPV6((host,port), MyTCPHandler)
    else:
        print("Error")
    server.serve_forever()

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    directions = socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM)
    print(directions, 'DIRECTIONS')
    connections = []
    for direction in directions:
        connections.append(threading.Thread(target=server, args=(direction, port)))
    for conection in connections:
        print(conection, 'conection')
        conection.start()