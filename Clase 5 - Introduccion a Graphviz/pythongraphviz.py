import graphviz

grafo = graphviz.Digraph('automata_finito', filename='AFD.dot')

grafo.attr(rankdir='LR', size='8,5')
# definimos todos los que queramos que sena invisibles
grafo.attr('node', style='invisible')
grafo.node('inv')
# definimos todos los que queramos que tengan forma de circulo
grafo.attr('node', shape='circle', style='')
grafo.node('q0')
# definimos todos los que queramos que tengan forma de doble circulo
grafo.attr('node', shape='doublecircle')
grafo.node('q1')

grafo.edge('inv', 'q0', label='inicio')
grafo.edge('q0:w', 'q0:n', label='0')
grafo.edge('q0:n', 'q1:n', label='1')
grafo.edge('q1:e', 'q1:n', label='1')
grafo.edge('q1:s', 'q0:s', label='0')

grafo.attr('node', shape='plaintext')

grafo.node('tabla1', '''<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
  <TR>
    <TD>left</TD>
    <TD PORT="f1">middle</TD>
    <TD PORT="f2">right</TD>
  </TR>
</TABLE>>''')

grafo.view()