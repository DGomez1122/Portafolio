#Potencia de un número

def potencia(n,n2):
    if isinstance(n,int) and isinstance(n2,int):
        if n>=0 and n2>=0:
            return AuxPotencia(n,n2,1)
    else:
        print("Ingrese numeros enteros positivos")

def AuxPotencia(n,n2,c):
    if c==n2:
        return n
    elif n==0:
        return 0
    elif n2==0:
        return 1
    else:
        return n * AuxPotencia(n,n2,c+1)
