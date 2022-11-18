import socketserver, subprocess, getopt, sys

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'h:p:a:')
    if len(opt) != 3:
        print("Por favor ingrese bien la cantidad de argumentos")
        exit()
except getopt.GetoptError as error:
    print(f'Error: {error}')
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

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            if len(data) == 0 or data == "bye":
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

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    if args == "p":
        server = Process((host, port), MyTCPHandler)
        print(f"Lanzando servidor con procesos (Port= {port})")
        server.serve_forever()
    elif args == "t":
        server = Thread((host, port), MyTCPHandler)
        print(f"Lanzando servidor con hilos (Port= {port})")
        server.serve_forever()