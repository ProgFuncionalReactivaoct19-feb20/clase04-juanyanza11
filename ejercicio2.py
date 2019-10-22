"""
	Encontrar la lista [('a', (30, 1)), ('b', (100, 2)), ('c', (20, 4))]
	author: juanyanza11
"""
lista = [(100,2),(20,4),(30,1)]
lista2= ("b","a","c")

newlist = list(zip(sorted(lista2, key = lambda x: x[0]), sorted(lista, key = lambda x: x[1])))
print(newlist)