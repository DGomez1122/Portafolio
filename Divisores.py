#Divisores de un número y los imprime de manera descendente

def divisores(n):
    if isinstance(n,int):
        return AuxDivisores(n,n)
    else:
        print("El número ingresado debe ser entero")
def AuxDivisores(n,div):
    if div==1:
        print(div)
    else:
        if n%div==0:
            print(div)
            return AuxDivisores(n,div-1)
        else:
            return AuxDivisores(n,div-1)
