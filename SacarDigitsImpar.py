#Función para sacar digitos impares de un número

def impares(n):
    if isinstance(n,int) and (n>=0):
        if n==0:
            return 0
        else:
            return auxImpar(n,0)
    else:
        print("Sólo se pueden ingresar numeros enteros positivos")
def auxImpar(n,n2):
    if n==0:
        return 0
    else:
        if (n%10)%2!=0:
            dig=(n%10)*10**n2
            return dig+auxImpar(n//10,n2+1)
        else:
            return auxImpar(n//10,n2)
