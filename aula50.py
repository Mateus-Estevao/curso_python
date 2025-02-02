""" 
For in com listas
"""

lista = ['Luiz', 'Otávio', 'Maria']
lista.append('Joaquim')
indices = range(len(lista))
print(indices)
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))   
    