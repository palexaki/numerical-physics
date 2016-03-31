from copy import deepcopy
cfile = open("/home/philippos/.config/numeric-phys/config","r")
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
            globals()[line[:foundc]] = float(line[variablest:])
        else:
            globals()[line[:foundc]] = float(line[variablest:variablend])


configurestart(cfile)
#globalsio = deepcopy(globals())
#for variable in globalsio:
print('\n'.join(repr((u,globals()[u])) for u in globals() if not u.startswith('__')))
