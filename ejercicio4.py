

paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]

promedios = list(map(lambda x: (x[0]+x[1]+x[2])/3,paraleloA))
promName = list(zip(promedios, nombres))
print(promName)