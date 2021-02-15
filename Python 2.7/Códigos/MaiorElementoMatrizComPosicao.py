#Leia uma matriz 5x5 e imprima o valor do mair elemento. Imprima também a
#linha e coluna desse elemento. 

matriz=[]
for i in range(0,5):
        matriz.append(0)
        matriz[i]=[]
        for j in range(0,5):
                matriz[i].append(input('Informe um numero: '))
print ''
for i in range(0,5):
        for j in range(0,5):
            print '%6.2f' %matriz[i][j],
        print ''

maior=matriz[0][0]
for i in range(0,5):
        for j in range(0,5):
                if maior<matriz[i][j]:
                        maior=matriz[i][j]
                        linha=i
                        coluna=j
print 'O maior numero digitado foi: ',maior
print 'Ele esta na linha',linha,'e na coluna',coluna

