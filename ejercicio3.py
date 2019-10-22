"""
	Ejercicio 3 presentar: [((20, 4), 'C'), ((30, 1), 'B'), ((100, 2), 'A')]
	author: juanyanza11
"""
lista = [(100,2), (20,4), (30,1)]
lista2 = ["b", "a", "c"]

lista3 = list(map(lambda x: x.upper(), lista2))
newlist = list(zip(sorted(lista), sorted(lista3, reverse = True)))
print(newlist)