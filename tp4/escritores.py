import getopt
import time
import sys
import os

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def hijo(letra: str):
    if not os.fork():
        if verboso:
            print(f"Proceso {os.getpid()} escribiendo letra \'{letra}\'")
        for i in range(len_letra):
            arch.write(letra)
            arch.flush()
            time.sleep(1)
        os._exit(0)


def escribir(name: str):
    arch = open(str(name), "w+")
    return arch


def leer(name: str):
    arch = open(str(name), "r")
    lines = arch.readlines()
    print(lines[0])

def ayuda() -> str:
    return f"Escritores\n\nargs:\n-n\tnumero de procesos hijos a crear\n-r\tnumero de veces que escribira el proceso" \
           f"\n-v\tmodo verbose\n-h\tmuestra este mensaje de ayuda\n-f\tpath del archivo (si no existe lo creara)\n"

try:
    (opt,arg) = getopt.getopt(sys.argv[1:], 'n:r:hf:v')
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

verboso = False
for (op,ar) in opt:
    if op == '-n':
        hijos = int(ar)
    if op == '-f':
        file = ar
    if op == '-r':
        len_letra = int(ar)
    if op == '-h':
        print(ayuda())
        sys.exit(0)
    if op == '-v':
        verboso = True

if __name__ == '__main__':

    arch = escribir(file)
    for i in range(hijos):
        hijo(ABC[i])

    for i in range(hijos):
        os.wait()

    leer(file)