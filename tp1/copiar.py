import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", type=str, required=False, help="string")
parser.add_argument("-o", "--other", type=str, required=False, help="string")
args = parser.parse_args()

try:
    file = open(args.file, "r")
    lines = file.readlines()
    file.close()

    copytext = open(args.other, "w")
    copytext.writelines(lines)
    copytext.close()
except FileNotFoundError:
    print("El archivo que ingreso no existe")