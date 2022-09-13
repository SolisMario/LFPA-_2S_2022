from Excepcion import Excepcion
import graphviz

letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s", "t", "u","v","w","x","y","z"]
numeros = ["1","2","3","4","5","6","7","8","9","0", "."]
tabla_errores = []

def recuperar_error(cadena, columna, fila):
    # se registra el error
    error_obj = Excepcion(fila, columna, "Lexico", cadena[0])
    tabla_errores.append(error_obj)

    # se recupera del error, desechando caracteres hasta encontrar
    # un delimitador, en este caso un ;
    res = cadena[:]
    caracter = res[0]

    while caracter != ';':
        res = res[1:]
        caracter = res[0]

    return res[1:]

def analizar(cadena):
    estado_actual = 0
    estado_anterior = 0

    columna = 0
    fila = 0

    # recorrer la cadena 
    while len(cadena) > 0:
        caracter = cadena[0]
        # ignorar espacios en blanco
        if caracter == ' ':
            columna += 1
            cadena = cadena[1:]
            continue

        # verificar el estado actual
        if estado_actual == 0:
            if caracter.lower() in letras:
                estado_actual = 0
                estado_anterior = 0
            elif caracter == '=':
                estado_actual = 1
                estado_anterior = 0
            else:
                res = recuperar_error(cadena, columna, fila)
                cadena = res

        elif estado_actual == 1:
            if caracter in numeros:
                estado_actual = 2
                estado_anterior = 1
        
        elif estado_actual == 2:
            if caracter in numeros:
                estado_actual = 2
                estado_anterior = 2
            elif caracter == '+':
                estado_actual = 4
                estado_anterior = 2
            elif caracter == ';':
                estado_actual = 3
                estado_anterior = 2

        elif estado_actual == 3:
            estado_actual = 0
            estado_anterior = 3

        elif estado_actual == 4:
            if caracter in numeros:
                estado_actual = 2
                estado_anterior = 4

        cadena = cadena[1:]
        columna += 1
        #  print(estado_anterior, '->', estado_actual)

def graficar_tabla():
    grafo = graphviz.Digraph('automata_finito', filename='AFD.dot')
    etiqueta = '''<
    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR>
        <TD>Fila</TD>
        <TD>Columna</TD>
        <TD>Tipo</TD>
        <TD>Error</TD>
    </TR>'''

    for error in tabla_errores:
        etiqueta += '<TR><TD>' + str(error.fila) + '</TD><TD>' + str(error.columna) + '</TD><TD>' + error.tipo + '</TD><TD>"' + error.error + '"</TD></TR>'

    etiqueta += '</TABLE>>'
    grafo.node('tabla1', etiqueta)

    grafo.view()

cadena = open('archivo.txt', 'r').read()
analizar(cadena)
graficar_tabla()