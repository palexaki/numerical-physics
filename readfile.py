from copy import deepcopy
import sys
cfile = open(sys.argv[1], 'r')
variables = {}
def configurestart(cfile):
    for line in cfile:
        line = line.rstrip()
        if "Formulas" in line:
            break
        foundc = line.find(":")
        if foundc == -1:
            raise SystemExit("FATAL ERROR IN LINE CONTAINING {}".format(line))
        variablest = foundc + 2
        variablend = line.find("'")
        if variablend == -1:
            variables[line[:foundc]] = float(line[variablest:])
        else:
            variables[line[:foundc]] = float(line[variablest:variablend])

def startformula(cfile):
    pass


configurestart(cfile)
print('\n'.join(repr((u,variables[u])) for u in variables if not u.startswith('__')))
