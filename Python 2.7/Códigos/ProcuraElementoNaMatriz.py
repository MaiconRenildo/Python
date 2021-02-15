#Leia uma matriz 4x4 e um valor X, procure a primeira vez que esse valor
#aparece na matriz imprimindo sua linha e coluna. Cason não exista o
#elemento, imprima uma mensagem de erro.

matriz=[]
for i in range(0,4):
    matriz.append(0)
    matriz[i]=[]
    for j in range(0,4):
        matriz[i].append(input('Informe um valor: '))

print ''
for i in range(0,4):
    print matriz[i]
print ''

achou=False
procurado=input('Informe o valor que voce deseja proxurar: ')
j=0
for i in range(0,4):
    while j<4:
        if procurado==matriz[i][j]:
            achou=True
            linha=i
            coluna=j
            j=3
        j+=1
if achou:
    print 'O numero foi encontrado na linha ',linha,'coluna',coluna
else:
    print 'O numero nao foi encontrado'

