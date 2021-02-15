#antissimetrica = sua transposta e igual a sua oposta

matriz = []

linhas = input('Quantidade de linhas na matriz: ')
colunas = input('Quantidade de colunas na matriz: ')

#criando a matriz
for i in range(0, linhas):
    matriz.append(0)
    matriz[i] = []
    for j in range(0, colunas):
        matriz[i].append(input('Digite um numero: '))

#criando a matriz transposta

transposta = []

for i in range(0, linhas):
    transposta.append(0)
    transposta[i] = []
    for j in range(0, colunas):
        transposta[i].append([])

#para printar a matriz no formato correto

print('Matriz original: ')

for i in range(0, linhas):
    for j in range(0, colunas):
        print "%4d" % matriz[i][j],
    print

#adicionando elementos da matriz a transposta

for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        transposta[j][i] = matriz[i][j]

#printando a transposta no formato correto

print('Matriz transposta:')

for i in range(0, len(transposta)):
    for j in range(0, len(transposta)):
        print "%4d" % transposta[i][j],
    print

#criando a estrutura da matriz oposta
oposta = []

for i in range(0, linhas):
    oposta.append(0)
    oposta[i] = []
    for j in range(0, linhas):
        oposta[i].append([])

#adicionando elementos a matriz oposta

for i in range(0, len(oposta)):
    for j in range(0, len(oposta)):
        oposta[i][j] = ((matriz[i][j])*(-1))

#printando a oposta no formato correto
print('Matriz oposta: ')

for i in range(0, len(oposta)):
    for j in range(0, len(oposta)):
        print "%4d" % oposta[i][j],
    print

#comparando os elementos das matrizes transposta e oposta

antissimetrica = True

for i in range(0, len(transposta)):
    for j in range(0, len(transposta)):
        if transposta[i][j] != oposta[i][j]:
            antissimetrica = False

if antissimetrica == False:
    print('As matrizes nao sao antissimetricas. ')
else:
    print('As matrizes sao antissimetricas. ')