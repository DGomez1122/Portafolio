#Función para saber el factorial de un número

def factorial(n):
    if isinstance(n,int) and (n>=0):
        if n==0:
            return 1
        else:
            return factorial(n-1)*n
    else:
        print("El número ingresado debe ser entero positivo")
