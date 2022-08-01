# crear clases y objetos
# palabra reservada class <<Nombre de clase>>
# dentro de esta van los atributos que esta tenga
# manera sin constructor
'''
class Person:
    name = ''
    department = ''
    birthday_month = ''
'''

# manera con constructor
class Persona:
    def __init__(self, name, department, birthday_month):
        self.name = name
        self.department = department
        self.birthday_month = birthday_month

    # esta puede tener funciones creadas en su interior
    def print_name(self):
        print(self.name)

    def print_department(self):
        print(self.department)

    def print_birthday_month(self):
        print(self.birthday_month)