import sys
import getopt


def sum(num1, num2):
    resultado = num1 + num2
    return resultado


def res(num1, num2):
    resultado = num1 - num2
    return resultado


def mul(num1, num2):
    resultado = num1 * num2
    return resultado


def div(num1, num2):
    resultado = num1 / num2
    return resultado


try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'o:m:n:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

oper = 0
num1 = 0
num2 = 0

try:
    for (op, ar) in opt:
        if (op in ['-o']):
            if (oper == 0):
                oper = ar
        elif (op == '-n'):
            if (num1 == 0):
                num1 = int(ar)
        elif (op == '-m'):
            if (num2 == 0):
                num2 = int(ar)
except ValueError:
    print("El argumento de -m y -n tiene que ser un numero")
    sys.exit()

try:
    if (oper == '+'):
        resultado = sum(num1, num2)
        print(num1, oper, num2, "=", resultado)
    elif (oper == '-'):
        resultado = res(num1, num2)
        print(num1, oper, num2, "=", resultado)
    elif (oper == 'x'):
        resultado = mul(num1, num2)
        print(num1, oper, num2, "=", resultado)
    elif (oper == '/'):
        resultado = div(num1, num2)
        print(num1, oper, num2, "=", resultado)
    else:
        print("Opcion invalida.")
except NameError:
    print("Calc.py necesita mas argumento para funcionar")