import os
import sys
import getopt

lineas = []

def leer():
    arch = open(file_to_read, 'r')
    return arch.readlines()

def hijo(line):
    if not os.fork():
        os.write(w, line[::-1].encode('ascii'))
        os._exit(0)
    else:
        value = os.read(r, 100)
        lineas.append(value.decode())

try:
    (opt,arg) = getopt.getopt(sys.argv[1:], 'f:')
except getopt.GetoptError as err:
    print(err)
    exit()

for (op,ar) in opt:
    if op == '-f':
        file_to_read = ar

if __name__ == '__main__':
    lines = leer()
    r, w = os.pipe()
    for line in lines:
        hijo(line)

    for line in lines:
        os.wait()

    for line in lineas:
        print(line)