"""
	Encontrar la siguiente estructura


[(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]
(16.666666666666668, 'José')
[(13.0, 'Ana'), (16.666666666666668, 'José'), (16.333333333333332, 'Ángel')]

"""
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]

promedios = list(map(lambda x: sum(x)/(len(x)),paraleloA))
promName1 = list(zip(promedios, nombres))
maximo = max(promName1)
promName2 = list((sorted(promName1, key = lambda x: x[1])))
print(promName1)
print(maximo)
print(promName2)