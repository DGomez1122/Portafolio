#Multiplicatoria entre 2 números (Manera recursiva sin operador)

def multiplicadorRecursivo(n,m):
    if isinstance(n,int) and isinstance(m,int):
        return AuxMulti(n,m)
    else:
        print("Los números ingresado debe ser entero")

def AuxMulti(n,m):
    if m==0:
        return 0
    elif m==1:
        return n
    else:
        return n + AuxMulti(n,m-1)
