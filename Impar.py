#Saber si un número es impar

def Impar(num):
    if isinstance(num,int) and (num>=0):
        return AuxImpar(num)
    else:
        print("El número ingresado debe ser entero positivo")

def AuxImpar(num):
    if num==0:
        print("El número cero es Neutro, no es par o impar")
    else:
        if num%2!=0:
            return True
        else:
            return False
