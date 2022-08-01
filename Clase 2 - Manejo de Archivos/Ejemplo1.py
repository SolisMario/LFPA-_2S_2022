# En Python, para abrir un archivo usaremos la función open, 
# que recibe el nombre del archivo a abrir.
archivo = open("archivo.txt")

# Esta función intentará abrir el archivo con el nombre indicado. 
# Si tiene éxito, devolverá una variable que nos permitirá manipular 
# el archivo de diversas maneras.

# Leer un archivo linea por linea
linea = archivo.readline()
archivo.close()

# Leer los archivos con ciclos
# esto nos permite leer archivos linea por linea procesando cada una
archivo = open("archivo.txt")
print(linea)
while linea != '':
    linea = archivo.readline();
    print(linea)
archivo.close()

archivo = open("archivo.txt")
for linea in archivo:
    print(linea)
archivo.close()

# Leer todas las lineas del archivo
archivo = open("archivo.txt")
lineas = archivo.readlines()
archivo.close()