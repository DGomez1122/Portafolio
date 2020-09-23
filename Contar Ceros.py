#Función para contar ceros

def contarceros(n):
    if isinstance(n,int):
        return auxContar(n)
    else:
        print("Error en parámetros de entrada, intente cambiar sus valores.")
def auxContar(n):
    if n<0:
        return auxContar(n*-1)
    elif n==0:
        return 0
    else:
        if n%10==0:
            return 1 + auxContar(n//10)
        else:
            return auxContar(n//10)
