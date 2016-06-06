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
        varst = foundc + 2
        varend = line.find("'")
        varname = line[:founc].rstrip().lstrip()
        if variablend == -1:
            variables[varname] = float(line[varst:])
        else:
            variables[varname] = float(line[varst:varend])

def startformula(cfile):
    pass


configurestart(cfile)
print('\n'.join(repr((u,variables[u])) for u in variables))
