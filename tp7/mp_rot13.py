from multiprocessing import Process, Queue, Pipe
import codecs
import sys
import os

def target_h1(c, q):
    sys.stdin = open(0)
    line = input()
    c.send(line)
    line_queue = q.get()
    print(f'H1: recuperando la linea encriptada desde la cola de mensajes: ({line_queue[:-1]})')

def target_h2(c, q):
    line = c.recv()
    line_rot13 = codecs.encode(line, 'rot_13')
    print(f'H2: ingresando la stdin ({line[:-1]}) encriptada con rot13 ({line_rot13[:-1]}) a la cola de mensajes')
    q.put(line_rot13)

def main():
    queue = Queue()
    a, b = Pipe()
    h1 = Process(target=target_h1, args=(a, queue))
    h2 = Process(target=target_h2, args=(b, queue))

    h1.start()
    h2.start()

    h1.join()
    h2.join()

if __name__ == '__main__':
    main()