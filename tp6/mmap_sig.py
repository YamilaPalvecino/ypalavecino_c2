import getopt
import signal
import mmap
import sys
import os


memoria = mmap.mmap(-1, 100)

def handler_padre(s, f):
    global continuar
    if s == signal.SIGUSR1:
        linea = memoria.readline()
        print(f'Padre: recibi de H1 la linea: {linea.decode()}')
        os.kill(h2, signal.SIGUSR1)
    if s == signal.SIGUSR2:
        print('Padre: aviso a H2 que tiene que terminar')
        continuar = False
        os.kill(h2, signal.SIGUSR2)

def handler_h2(s, f):
    if s == signal.SIGUSR1:
        linea = memoria.readline()
        print(f'H2: recibi la señal de mi Padre, leyendo y almacenando la linea: {linea.decode()}')
        with open(path, 'a') as archivo:
            archivo.write(linea.decode().upper())
            archivo.flush()
    if s == signal.SIGUSR2:
        print('H2: avisando a Padre y terminando...')
        os._exit(0)

try:
    (opt,arg) = getopt.getopt(sys.argv[1:], 'f:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

for (op,ar) in opt:
    if op == '-f':
       path = str(ar)

h1 = os.fork()
if h1 == 0:
    print(f'Soy H1, mi pid es: {os.getpid()} y el pid de mi padre es: {os.getppid()}')
    for linea in sys.stdin:
        if linea == 'bye\n':
            print('H1: enviando señal a Padre y terminando...')
            os.kill(os.getppid(), signal.SIGUSR2)
            os._exit(0)
        else:
            print(f'H1: recibi la linea: {linea}')
            memoria.write(linea.encode('ascii'))
            os.kill(os.getppid(), signal.SIGUSR1)

h2 = os.fork()
if h2 == 0:
    print(f'Soy H2, mi pid es: {os.getpid()} y el pid de mi padre es: {os.getppid()}\n')
    signal.signal(signal.SIGUSR1, handler_h2)
    signal.signal(signal.SIGUSR2, handler_h2)
    while True:
        signal.pause()

continuar = True
print(f'Soy el Padre, mi pid es: {os.getpid()}')
signal.signal(signal.SIGUSR1, handler_padre)
signal.signal(signal.SIGUSR2, handler_padre)

while continuar:
    signal.pause()
else:
    for i in range(2):
        os.wait()
    print('Padre: terminando...')