#Función para sacar digitos pares de un número

def pares(n):
    if isinstance(n,int) and (n>=0):
        if n==0:
            return 0
        else:
            return auxpar(n,0)
    else:
        print("Sólo se pueden ingresar numeros enteros positivos")
def auxpar(n,n2):
    if n==0:
        return 0
    else:
        if (n%10)%2==0:
            dig=(n%10)*10**n2
            return dig+auxpar(n//10,n2+1)
        else:
            return auxpar(n//10,n2)
