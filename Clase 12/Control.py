class Control:
    def __init__(self, tipo, nombre):
        self.tipo = tipo
        self.nombre = nombre

    def transformar(self):
        if (self.tipo.lower() == 'etiqueta'):
            return '<label id="' + self.nombre + '"></label>'
        elif (self.tipo.lower() == 'boton'):
            return '<button id="' + self.nombre + '"></button>'
