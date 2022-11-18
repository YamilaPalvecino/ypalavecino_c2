import os, sys, click
from celery import pot, log, raiz
from celery.result import AsyncResult

@click.command()
@click.option('-f', '--file', 'file', help='Ruta al archivo de texto', required=True)
@click.option('-c', '--calc', 'calc', help='Funcion de calculo', required=True)

def main(file, calc):
    if not os.path.exists(file):
        print("El archivo no existe")
        sys.exit(1)
    if calc not in ['raiz', 'pot', 'log']:
        print("Función no válida")
        sys.exit(1)
    with open(file, 'r') as f:
        new_matrix = []
        for line in f:
            new_line = []
            for num in line.split(","):
                if calc == 'raiz':
                    resultado = raiz.delay(int(num))
                elif calc == 'pot':
                    resultado = pot.delay(int(num))
                elif calc == 'log':
                    resultado = log.delay(int(num))
                res = AsyncResult(resultado.id)
                new_line.append(res.get())
            new_matrix.append(new_line)
        print(f"Matriz resultante: \n{new_matrix}\n")

if __name__=="__main__":
    main()