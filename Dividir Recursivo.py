#Divide 2 números (Manera recursiva sin operdor)

def dividirRecursivo(dividendo,divisor):
    if isinstance(dividendo,int) and isinstance(divisor,int):
        if divisor==0:
            print("Imposible dividir entre cero")
        else:
            return AuxDividir(dividendo,divisor)
    else:
        print("Los números ingresado debe ser entero")

def AuxDividir(dividendo,divisor):
    if dividendo==divisor:
        return 1
    elif dividendo<divisor:
        return 0
    else:
        return 1 + AuxDividir(dividendo-divisor,divisor)
    
