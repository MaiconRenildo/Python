#Leia uma matriz 7x7 e imprima a soma dos elementos da linha 6.
#Imprima tambem a soma dos elementos da coluna 2. Imprima também
#a soma dos elementos da diagonal principal. Imprima também o
#elemento da linha 3 e  coluna 4. Imprima também a soma de todos
#os elementos pares da matriz.

matriz=[]
for i in range(0,7):
    matriz.append(0)
    matriz[i]=[]
    for j in range(0,7):
        matriz[i].append(input('Informe o valor: '))

print ''
for i in range(0,7):
        for j in range(0,7):
            print '%3d' %matriz[i][j],
        print ''



somaLinha6=0
somaColuna2=0
somaPares=0
somaDiagonalPrincipal=0

for i in range(0,7):
    for j in range(0,7):
        if i==j:
            somaDiagonalPrincipal+=matriz[i][j]
        if matriz[i][j]%2==0:
            somaPares+=matriz[i][j]
        if i==6:
            somaLinha6+=matriz[i][j]
        if j==2:
            somaColuna2+=matriz[i][j]
        if i==3 and j==4:
            print 'Elemento da linha 3 coluna 4',matriz[i][j]
print 'Soma da Diagonal principal: ',somaDiagonalPrincipal
print 'Soma dos elementos pares: ',somaPares
print 'Soma dos elementos da linha 6: ',somaLinha6
print 'Soma dos elementos da coluna 2: ',somaColuna2



