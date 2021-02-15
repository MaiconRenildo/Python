#soma de matrizes (mesmas dimensoes)

matrizA = []
matrizB = []

linhas = input('Quantidade de linhas das matrizes: ')
colunas = input('Quantidade de colunas das matrizes: ')

#criando a estrutura da matriz A
for i in range(0, linhas):
    matrizA.append(0)
    matrizA[i] = []
    for j in range(0, colunas):
        matrizA[i].append(input('Digite o elemento da matriz A: '))

#criando a estrutura da matriz B

for i in range(0, linhas):
    matrizB.append(0)
    matrizB[i] = []
    for j in range(0, colunas):
        matrizB[i].append(input('Digite o elemento da matriz B: '))

#printando as matrizes no formato correto

print('Matriz A: ')

for i in range(0, len(matrizA)):
    for j in range(0, len(matrizA)):
        print "%4d" % matrizA[i][j],
    print

print('Matriz B: ')

for i in range(0, len(matrizB)):
    for j in range(0, len(matrizB)):
        print "%4d" % matrizB[i][j],
    print

#criando a matriz soma

soma = []

for i in range(0, len(matrizA)):
    soma.append(0)
    soma[i] = []
    for j in range(0, len(matrizA)):
        soma[i].append((matrizA[i][j])+(matrizB[i][j]))

#printando a matriz soma

print('Matriz soma: ')

for i in range(0, len(soma)):
    for j in range(0, len(soma)):
        print "%4d" % soma[i][j],
    print

