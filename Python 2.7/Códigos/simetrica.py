#simetrica = igual a sua transposta

#matriz transposta: as linhas viram colunas e as colunas viram linhas

matriz = []
transposta = []

linhas = input('Quantidade de linhas na matriz: ')
colunas = input('Quantidade de colunas na matriz: ')

#criando a matriz
for i in range(0, linhas):
    matriz.append(0)
    matriz[i] = []
    for j in range(0, colunas):
        matriz[i].append(input('Digite um numero: '))

#criando a matriz transposta
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

#Para conferir se e transposta, isto e, se todos os is e js sao iguais entre as matrizes

simetrica = True

for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        if matriz[i][j] != transposta[i][j]:
            simetrica = False

if simetrica == False:
    print('As matrizes nao sao simetricas. ')
else:
    print('As matrizes sao simetricas. ')
