#Función que dice si un número tiene ceros o no

def tieneceros(n):
    if isinstance(n,int) and n>=0:
        if n==0:
            return True
        else:
            return AuxTieneCeros(n)
    else:
        print("Error en parámetros de entrada, el número deber ser entero y positivo.")

def AuxTieneCeros(n):
    if n==0:
        return False
    else:
        if (n%10)==0:
            return True
        else:
            return AuxTieneCeros(n//10)
