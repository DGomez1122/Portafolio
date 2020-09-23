#Sumatoria con inicio, fin y rango

def sumatoriaRangos(inicio,fin,rango):
    if isinstance(inicio,int) and isinstance(fin,int) and isinstance(rango,int):
        return AuxSumatoriaR(inicio,fin,rango)
    else:
        print("Error en datos de entrada, deben ser números enteros")
def AuxSumatoriaR(inicio,fin,rango):
    if fin<inicio:
        return 0
    else:
        return inicio+AuxSumatoriaR(inicio+rango,fin,rango)
