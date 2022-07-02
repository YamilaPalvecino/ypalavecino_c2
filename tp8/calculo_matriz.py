from multiprocessing import Pool
from math import sqrt, log10
from functools import partial
import getopt
import sys


def leer_matriz(path):
    with open(path, 'r') as file:
        matriz = file.readlines()
        matriz = [line.split(',') for line in matriz]
        return matriz

def calculator(fun, matriz):
    matriz_nueva: list= []
    for fila in matriz:
        nueva_fila = []
        for elemento in fila:
            elemento = calculate(fun, elemento)
            nueva_fila.append(elemento)
        matriz_nueva.append(nueva_fila)
    return matriz_nueva

def log(elemento):
    return log10(int(elemento))

def raiz(elemento):
    return sqrt(int(elemento))

def pot(elemento):
    return int(elemento)**int(elemento)

def calculate(fun, elemento):
    functions = {
        'pot': pot(elemento),
        'raiz': raiz(elemento),
        'log': log(elemento)
    }
    return functions[fun]

def main():
    pool = Pool(processes=num_process)
    results = pool.starmap(partial(calculator, calc), [[leer_matriz(path=path)]])
    print(results[0])

try:
    (opt,arg) = getopt.getopt(sys.argv[1:], 'p:f:c:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

for (op,ar) in opt:
    if op == '-p':
       num_process = int(ar)
    if op == '-f':
        path = str(ar)
    if op == '-c':
        calc = str(ar)

if __name__ == '__main__':
    main()