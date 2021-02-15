#Leia uma matriz 3x3 e imprima a soma dos elementos da diagonal
#principal e a soma dos elementos da diagonal secundária.

matriz=[]
for i in range(0,3):
    matriz.append(0)
    matriz[i]=[]
    for j in range(0,3):
        matriz[i].append(input('Informe o valor: '))

for i in range(0,3):
    print matriz[i]

somaDP=0
somaDS=0
for i in range(0,3):
    for j in range(0,3):
        if i==j:
            somaDP+=matriz[i][j]
        if i+j==2:
            somaDS+=matriz[i][j]
print 'A soma dos elementos da DP eh: ',somaDP
print 'A soma dos elementos da DS eh: ',somaDS
