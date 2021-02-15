#Leia uma matriz 4x4 e troque os valores da 2 linha pelo da quarta
#coluna.Imprima a matriz original e a matriz trocada.

#Linha 2-> indice 2
#4a coluna-> indice 3
matriz=[]
for i in range(0,4):
    matriz.append(0)
    matriz[i]=[]
    for j in range(0,4):
        matriz[i].append(input('Informe o valor: '))

print 'Matriz original: '
print ''        
for i in range(0,4):
    print matriz[i]
print ''

aux=[]
for i in range(0,4):
    for j in range(0,4):
        if i==2:
            aux.append(matriz[i][j])
            matriz[i][j]=matriz[j][3]            
print aux
for i in range(0,4):
    for j in range(0,4):
        if j==3:
            matriz[i][3]=aux[i]

print 'Matriz Trocada: '
print ''        
for i in range(0,4):
    print matriz[i]
print ''
