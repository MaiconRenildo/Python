#multiplicar por numero inteiro -> multiplica todos os elementos

matriz = []

linhas = input('Quantidade de linhas na matriz: ')
colunas = input('Quantidade de colunas na matriz: ')

for i in range(0, linhas):
    matriz.append(0)
    matriz[i] = []
    for j in range(0, colunas):
        matriz[i].append(input('Digite um numero: '))

inteiro = input('Digite um numero inteiro: ')

#criando a estrutura da matriz produto

produtoMatriz = []

for i in range(0, linhas):
    produtoMatriz.append(0)
    produtoMatriz[i] = []
    for j in range (0, colunas):
        produtoMatriz[i].append(inteiro*(matriz[i][j]))
#para printar a matriz no formato correto

print('Matriz original: ')

for i in range(0, linhas):
    for j in range(0, colunas):
        print "%4d" % matriz[i][j],
    print

#printando a matriz produto

print('Matriz produto por escalar: ')

for i in range(0, linhas):
    for j in range(0, colunas):
        print "%4d" % produtoMatriz[i][j],
    print