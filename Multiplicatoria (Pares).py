#Multiplicar números pares

def multiplicatoria(n):
    if isinstance(n,int) and (n>=0):
        return AuxMulti(n)
    else:
        print("El valor ingresado debe ser entero y positivo")

def AuxMulti(n):
    if n==0:
        return 1
    elif (n%2)==0:
        return n * multiplicatoria(n-1)
    else:
        return multiplicatoria(n-1)




