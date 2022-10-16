from Control import Control


letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s", "t", "u","v","w","x","y","z"]
numeros = ["1","2","3","4","5","6","7","8","9","0", "."]
rControles = ['etiqueta', 'boton', 'check', 'radioBoton']
controles = []
    
def analizar(cadena):
    estadoActual = 0
    estadoAnterior = 0
    comentarioUnilinea = False;
    comentarioMultilinea = False;
    caracter = ''
    etiquetaComentario = '' # guardar */
    lexema = ''
    slash = False

    tipoControl = ''

    while cadena.length > 0:

        if comentarioUnilinea: # se activa cuando se reconoce //
            if caracter == '\n':
                comentarioUnilinea = False
                continue
            else:
                continue
        
        if comentarioMultilinea: # se activa cuando se reconoce /*
            if etiquetaComentario == '*\\':
                comentarioMultilinea = False
                continue
            else:
                if len(etiquetaComentario) == 0:
                    etiquetaComentario = caracter
                elif len(etiquetaComentario) == 1:
                    etiquetaComentario += caracter
                else:
                    etiquetaComentario = etiquetaComentario[1] + caracter
                continue

        if estadoActual == 0:
            if caracter == '<':
                estadoActual = 1
                estadoAnterior = 0
        elif estadoActual == 1:
            if caracter == '!':
                estadoActual = 2
                estadoAnterior = 1
        elif estadoActual == 2:
            if caracter == '-':
                estadoActual = 3
                estadoAnterior = 2
        elif estadoActual == 3:
            if caracter == '-':
                estadoActual = 4
                estadoAnterior = 3
        elif estadoActual == 4:
            if caracter in letras:
                estadoActual = 4
                estadoAnterior = 4
            elif caracter == ' ' or caracter == '\n':
                if validarSintaxis(['<!--controles'], lexema):
                    lexema = ''
                    estadoActual = 5
                    estadoAnterior = 4
                else:
                    pass
        elif estadoActual == 5:
            if caracter in letras:
                estadoActual = 5
                estadoAnterior = 5
            elif caracter == ' ':
                if validarSintaxis(rControles, lexema):
                    estadoActual = 6
                    estadoAnterior = 5
                    tipoControl = lexema
                    lexema = ''
                else:
                    pass
        elif estadoActual == 6:
            if caracter in letras:
                estadoActual = 6
                estadoAnterior = 6
            elif caracter == ';':
                control = Control(tipoControl, lexema)
                lexema = ''
        elif estadoActual == 7:
            pass
        elif estadoActual == 8:
            pass
        elif estadoActual == 9:
            pass
        elif estadoActual == 10:
            pass
        elif estadoActual == 11:
            pass
        elif estadoActual == 12:
            pass
        elif estadoActual == 13:
            pass
        elif estadoActual == 14:
            pass

        lexema += caracter

def validarSintaxis(reservadas, lexema):
    if lexema.lower() in reservadas:
        return True
    return False