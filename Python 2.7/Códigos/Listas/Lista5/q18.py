#Leia uma matriz 6x6 e conte quantos elementos maiores que 10 existem
#na matriz. Imprima esse valor e a matriz.

matriz=[]
for i in range(0,6):
    matriz.append(0)
    matriz[i]=[]
    for j in range(0,6):
        matriz[i].append(input('Informe um valor: '))

print ''
for i in range(0,6):
    print matriz[i]
print ''

contador=0
for i in range(0,6):
    for j in range(0,6):
        if matriz[i][j]>10:
            print ' O numero ',matriz[i][j],'eh maior que 10'
            contador+=1
print 'Foram encontrados',contador,'numeros maiores que 10'
