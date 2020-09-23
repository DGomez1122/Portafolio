#Sumatoria de un número dado su inicio y final

def sumatoriaNaM(inicio,fin):
    if isinstance(inicio,int) and isinstance(fin,int):
        if (inicio>=0) and (fin>=0):
            return AuxSumatoria(inicio,fin)
    else:
        print("Error en datos de entrada, intente cambiarlos")
def AuxSumatoria(inicio,fin):
    if fin<inicio:
        return 0
    else:
        return inicio+AuxSumatoria(inicio+1,fin)
