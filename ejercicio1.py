"""
	presentar [(2, 'd'), (3, 'c'), (4, 'b'), (10, 'a')]
			  maximo: (10, 'a')
"""
listaA = [10,2,3,4]
listaB = ["a","b","c","d"]

listaA = sorted(listaA)
listaB = sorted(listaB, reverse = True) # Condicion para revertir el orden de las palabras

result = list(zip(listaA,listaB)) # Hacer lista usando funcion zip 
maximo = max(result) # Funcion para sacar el maximo en las tuplas
print(result)
print(maximo)
