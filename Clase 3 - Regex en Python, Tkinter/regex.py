# importando el modulo de regex de python
import re  

# compilando la regex
# patron = re.compile(r'\bfoo\b')  # busca la palabra foo
patron = re.compile(r'/^[a-z0-9_-]{3,16}$/')  # busca la palabra foo

# texto de entrada
texto = """ bar foo bar
foo barbarfoo
foofoo foo bar
"""
texto = 'us3r_n4m3'
# match nos devuelve None porque no hubo coincidencia al comienzo del texto
print(patron.match(texto))

# match encuentra una coindencia en el comienzo del texto
m = patron.match('foo bar')
print(m)

# search nos devuelve la coincidencia en cualquier ubicacion.
s = patron.search(texto)
print(s)


# findall nos devuelve una lista con todas las coincidencias
fa = patron.findall(texto)
print(fa)

# finditer nos devuelve un iterador
fi = patron.finditer(texto)
'''for ap in fi:
    print(ap)'''

# TODOS DEVUELVEN EL OBJETO DE COINCIDENCIA EXCEPTO findall

# METODOS DE LOS OBJETOS DE COINCIDENCIA

# group(): devuelve el texto que coincide con la expresion regular.
# start(): devuelve la posición inicial de la coincidencia.
# end(): devuelve la posición final de la coincidencia.
# span(): devuelve una tupla con la posición inicial y final de la coincidencia.

# Métodos del objeto de coincidencia
for m in fi:
    print(m.group(), m.start(), m.end(), m.span())