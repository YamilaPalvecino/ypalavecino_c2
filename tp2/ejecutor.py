import os
import sys
import getopt
import subprocess as sp
from datetime import datetime


def outputfile(outfile):
    if arch1 is True:
        outf = open(outfile, "a")
        outf.writelines(stdout)
    else:
        outf = open(outfile, "w")
        outf.writelines(stdout)


def log_file(logfile):
    correcto = (str(fecha)+": Comando \""+command+"\" ejecutado correctamente\n")
    error = (str(fecha)+" "+stderr)
    if arch2 is True:
        logf = open(logfile, "a")
        if (c.returncode == 0):
            logf.writelines(correcto)
        elif (c.returncode != 0):
            logf.writelines(error)
    else:
        logf = open(logfile, "w")
        if (c.returncode == 0):
            logf.writelines(correcto)
        elif (c.returncode != 0):
            logf.writelines(error)


try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'c:f:l:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

command = 0
outfile = 0
logfile = 0

for (op, ar) in opt:
    if (op in ['-c']):
        if (command == 0):
            command = ar
    elif (op == '-f'):
        if (outfile == 0):
            outfile = ar
    elif (op == '-l'):
        if (logfile == 0):
            logfile = ar

if (command == 0 or outfile == 0 or logfile == 0):
    print("faltan opciones")
    sys.exit()
else:
    c = sp.Popen([command], shell=True, stdout=sp.PIPE, stderr=sp.PIPE, text=True)
    stdout, stderr = c.communicate()

    arch1 = os.path.isfile(outfile)
    arch2 = os.path.isfile(logfile)

    fecha = datetime.now()
    outputfile(outfile)
    log_file(logfile)