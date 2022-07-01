import os
import sys
import getopt

def hijo():
    if not os.fork():
        suma = sum([i for i in range(os.getpid()) if i % 2 == 0])
        if verboso:
            print(f"Iniciando proceso hijo {os.getpid()}")
            print(f'{os.getpid()} - {os.getppid()}: {suma}')
            print(f"Finalizando proceso hijo {os.getpid()}")
        else:
            print(f'{os.getpid()} - {os.getppid()}: {suma}')
        os._exit(0)

def ayuda() -> str:
    return f"Suma pares\n\nargs:\n-n\tnumero de procesos hijos a crear\n-v\tmodo verbose\n-h\tmuestra este mensaje de ayuda"

try:
    (opt,arg) = getopt.getopt(sys.argv[1:], 'n:hv')
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

verboso = False
for (op,ar) in opt:
    if op == '-n':
        hijos = int(ar)
    elif op == '-h':
        print(ayuda())
        sys.exit(2)
    elif op == '-v':
        verboso = True

for i in range(hijos):
    hijo()
for i in range(hijos):
    os.wait()