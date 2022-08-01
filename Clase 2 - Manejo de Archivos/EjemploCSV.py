# importamos la libreria csv para realizar operaciones con estos archivos
import csv
# importamos nuestra clase persona
from Persona import Persona

# se crea la lista que contendra nuestros objetos
people = []

# leer los archivos csv
# with open(<<nombrearchivo.extension>>, <<modo de lectura>>)
# as <<nombre de variable donde se guarda el archivo>>
# delimiter para definir como se separan las columnas
# se obtiene cada linea con la funcion reader
csvfile = open('datos.csv', 'r')
reader = csv.reader(csvfile, delimiter=',')

# utilizar los datos de cada fila del csv
for row in reader:
    name = row[0]
    department = row[1]
    birthday_month = row[2]
    print(name, department, birthday_month)
    new_person = Persona(name, department, birthday_month)
    people.append(new_person)

# utilizando las funciones de la clase para imprimir los datos
for person in people:
    person.print_name()
    person.print_department()
    person.print_birthday_month()