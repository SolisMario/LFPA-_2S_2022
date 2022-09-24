from Token import Token
from Operacion import Operacion

class Automata:
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s", "t", "u","v","w","x","y","z"]
    numeros = ["1","2","3","4","5","6","7","8","9","0", "."]
    tabla_tokens = []
    cadena = ''
    fila = 0
    columna = 0
    estado_actual = 0
    estado_anterior = 0


    def analizar(self, cadena, operacion:Operacion):
        etiqueta_abre = ''
        etiqueta_cierra = ''
        token = ''
        operaciones = []
        cierre = False

        # recorrer cadena
        while len(cadena) > 0:
            char = cadena[0]

            # ignorar espacios en blanco o saltos de linea
            if char == '\n':
                self.fila += 1
                self.columna = 0
                cadena = cadena[1:]
                continue
            elif char == ' ':
                self.columna += 1
                cadena = cadena[1:]
                continue

            # verificar estado actual
            if self.estado_actual == 0:
                if char == '<':
                    self.guardar_token(char)

                    self.estado_actual = 1
                    self.estado_anterior = 0
            elif self.estado_actual == 1:
                if char.lower() in self.letras:
                    token += char

                    self.estado_actual = 1
                    self.estado_anterior = 1
                elif char == '>':
                    self.guardar_token(token)
                    self.guardar_token(char)

                    if cierre:
                        etiqueta_cierra = token
                        cierre = False

                        if etiqueta_cierra.lower() == 'operacion':
                            operacion.operandos = operaciones
                            return [cadena, operacion]

                    if etiqueta_abre.lower() == 'operacion':
                        op = Operacion(token)
                        valor = self.analizar(cadena[1:], op)
                        cadena = valor[0]
                        operaciones.append(valor[1])
                    
                    etiqueta_abre = token
                    token = ''

                    self.estado_actual = 2
                    self.estado_anterior = 1
                elif char == '=':
                    etiqueta_abre = token

                    self.guardar_token(token)
                    self.guardar_token(char)
                    token = ''

                    self.estado_actual = 3
                    self.estado_anterior = 1
                elif char == '/':
                    cierre = True
                    self.guardar_token(char)

                    self.estado_actual = 5
                    self.estado_anterior = 1
            elif self.estado_actual == 2:
                if char in '<':
                    self.guardar_token(char)

                    self.estado_actual = 1
                    self.estado_anterior = 2
                elif char in self.numeros:
                    token += char

                    self.estado_actual = 4
                    self.estado_anterior = 2
            elif self.estado_actual == 3:
                if char.lower() in self.letras:
                    token += char

                    self.estado_actual = 1
                    self.estado_anterior = 3
            elif self.estado_actual == 4:
                if char in '<':
                    if etiqueta_abre.lower() == 'numero':
                        operaciones.append(token)

                    self.guardar_token(token)
                    self.guardar_token(char)
                    token = ''

                    self.estado_actual = 1
                    self.estado_anterior = 4
                elif char in self.numeros:
                    token += char

                    self.estado_actual = 4
                    self.estado_anterior = 4
            elif self.estado_actual == 5:
                if char.lower() in self.letras:
                    token += char
                    self.estado_actual = 1
                    self.estado_anterior = 5

            # print(self.estado_anterior, '->', self.estado_actual)
            self.columna += 1
            cadena = cadena[1:]

        operacion.operandos = operacion
        return [cadena, operaciones]
    
    def guardar_token(self, lexema):
        nuevo_token = Token(self.fila, self.columna, lexema)
        self.tabla_tokens.append(nuevo_token)

    def imprimir_tokens(self):
        print('-'*31)
        print ("| {:<4} | {:<7} | {:<10} |".format('Fila','Columna','Lexema'))
        print('-'*31)
        for token in self.tabla_tokens:
            print ("| {:<4} | {:<7} | {:<10} |".format(token.fila, token.columna, token.lexema))


autom = Automata()
cadena = open('archivo.txt', 'r').read()

resultado = autom.analizar(cadena, Operacion('suma'))

for oper in resultado[1]:
    resultado = oper.operar()
    print(resultado[0], "=", resultado[1])

autom.imprimir_tokens()
