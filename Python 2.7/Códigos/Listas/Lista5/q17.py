#Crie uma matriz 5x5 com 1 na diagonal principal e 0 nas outras posições.
#Imprima a matriz.

matriz=[]
for i in range(0,5):
    matriz.append(0)
    matriz[i]=[]
    for j in range(0,5):
        if i==j:
            matriz[i].append(1)
        else:
            matriz[i].append(0)

for i in range(0,5):
    print matriz[i]

