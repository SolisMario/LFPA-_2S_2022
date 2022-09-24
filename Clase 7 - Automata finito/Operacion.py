from webbrowser import Opera


class Operacion:
    def __init__(self, tipo):
        self.tipo = tipo
        self.operandos = []

    def operar(self):
        res = ''
        resnum = 0
        if self.tipo.lower() == 'suma':
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' + '
                    resnum += float(operando)
                else:
                    operado = operando.operar()
                    res += "(" + operado[0] + ") + "
                    resnum += operado[1]

        elif self.tipo.lower() == 'multiplicacion':
            resnum = 1
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' * '
                    resnum = resnum * float(operando)
                else:
                    res += "(" + operando.operar() + ") * "
                    resnum = resnum * float(operado[1])
        
        return [res[0:-3], resnum]