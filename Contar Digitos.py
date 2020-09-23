#Cuenta cuántos dígitos se encuentran en un número

def ContarDigitos(num):
    if isinstance(num,int):
        return AuxContar(num)
    else:
        print("El valor ingresado deber ser un número entero")
def AuxContar(num):
    if num<10:
        return 1
    else:
        return 1+AuxContar(num//10)
