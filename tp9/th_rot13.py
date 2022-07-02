from threading import Thread
import codecs
import sys
import os

def leer(w):
    print('Ingrese texto a cifrar: ')
    sys.stdin = open(0)
    linea = input()
    os.write(w, linea.encode("ascii"))

def escribir(r):
    linea = os.read(r, 100).decode()
    linea_encode = codecs.encode(linea, 'rot_13')
    print(f'Texto cifrado: {linea_encode}')

def main():
    r, w = os.pipe()
    t1 = Thread(target=leer, args=(w,))
    t2 = Thread(target=escribir, args=(r,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == '__main__':
    main()