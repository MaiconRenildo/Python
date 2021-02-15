#matriz oposta - os sinais de todos os elementos estao invertidos

matriz = []

linhas = input('Quantidade de linhas na matriz: ')
colunas = input('Quantidade de colunas na matriz: ')

for i in range(0, linhas):
    matriz.append(0)
    matriz[i] = []
    for j in range(0, colunas):
        matriz[i].append(input('Digite um numero: '))

#para printar a matriz no formato correto

for i in range(0, linhas):
    for j in range(0, colunas):
        print "%4d" % matriz[i][j],
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