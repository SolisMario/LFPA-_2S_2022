# IMPORTAR LIBRERIA
import tkinter as tk

# ----------------------------------------------------------------------------------
#                       ETIQUETAS
# ----------------------------------------------------------------------------------
# ETIQUETA CON GRID, POSICIONAR COMO TABLA
def Etiqueta1(_ventana:tk, _fila:int, _columna:int, _texto:str):
    lbl = tk.Label(_ventana, text=_texto)
    lbl.grid(column=_columna, row=_fila)

# ETIQUETA CON PLACE, POSICIONAR CON PIXELES
def Etiqueta2(_ventana:tk, _x:int, _y:int, _texto:str):
    tk.Label(_ventana, text=_texto).place(x=_x, y=_y)

# ETIQUETA CON FORMATO
def Etiqueta3(_ventana:tk, _x:int, _y:int, _texto:str):
    tk.Label(_ventana, text=_texto, font=("Arial Black", 12)).place(x=_x, y=_y)


# LABEL MODIFICABLE
def Etiqueta4(_ventana:tk, _x:int, _y:int, _texto:str):
    tk.Label(_ventana, textvariable=_texto, font=("Arial Black", 12)).place(x=_x, y=_y)


# ----------------------------------------------------------------------------------
#                       ACCIONES DE BOTONES
# ----------------------------------------------------------------------------------
def metodo1(_ventana):
    Etiqueta3(_ventana, 100, 100, "Mensaje modificable")

def metodo2(_ventana, _stringvar:tk.StringVar, _texto:str):
    _stringvar.set(_texto)

# ----------------------------------------------------------------------------------
#                       ENTRADAS DE TEXTO
# ----------------------------------------------------------------------------------
def Entrada(_ventana, _x:int, _y:int):
    res = tk.StringVar()
    tk.Entry(_ventana, width=20, textvariable=res).place(x=_x, y=_y)
    return res



    


# ----------------------------------------------------------------------------------
#                       MAIN
# ----------------------------------------------------------------------------------
def main(_ventana:tk):
    # CREAR UNA VENTANA
    ventana = _ventana

    # AGREGAR UN TITULO A LA VENTANA
    ventana.title("Ejemplo de interfaz")
    
    # TAMAÑO DE LA VENTANA
    ventana.geometry('700x700')
    ventana.resizable(width=0, height=0)

    Etiqueta1(ventana, 0, 0, "Hola estudiantes de Lenguajes Formales")
    Etiqueta2(ventana, 100, 50, "100px X 100px")

    # USAMOS STRINGVAR PARA HACER UN TEXTO MODIFICABLE
    texto_mod = tk.StringVar()
    texto_mod.set("Texto antiguo")
    Etiqueta4(ventana, 100, 150, texto_mod)

    # BOTONES
    tk.Button(ventana, text="Visualizar Texto", width=0, anchor="c", font=("Arial", 12),  command=lambda : metodo1(ventana)).place(x=100, y=300)
    tk.Button(ventana, text="Remplazar Texto Antiguo", width=0, anchor="c", font=("Arial", 12),  command=lambda : metodo2(ventana, texto_mod, "Nuevo")).place(x=100, y=350)
    tk.Button(ventana, text="Remplazar Texto Nuevo", width=0, anchor="c", font=("Arial", 12),  command=lambda : metodo2(ventana, texto_mod, "Antiguo")).place(x=100, y=400)


    # ENTRADAS DE TEXTO
    entrada1 = Entrada(ventana, 100, 500)
    entrada1.set("Hola")
    tk.Button(ventana, text="Enviar", width=0, anchor="c", font=("Arial Black", 12),  command=lambda : metodo2(ventana, entrada1, "Adios")).place(x=100, y=550)



    # ACTIVAR/MOSTRAR VENTANA
    ventana.mainloop()


# LLAMEMOS AL METODO MAIN
main(tk.Tk())


