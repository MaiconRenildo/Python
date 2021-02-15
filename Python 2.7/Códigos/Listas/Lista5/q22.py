#Leia uma matriz 4x4 e troque os elementos da diagonal principal com os
#elementos da diagonal secundária.Imprima a matriz original e a matriz
#secundária.

matriz=[]
for i in range(0,4):
    matriz.append(0)
    matriz[i]=[]
    for j in range(0,4):
        matriz[i].append(input('Informe um valor: '))

print 'Matriz Inicial'
print ''
for i in range(0,4):
    print matriz[i]
print ''

principal=[]
secundario=[]
for i in range(0,4):
    for j in range(0,4):
        if j==i:
            principal.insert(0,matriz[i][j])
        if j+i==3:
            secundario.insert(0,matriz[i][j])

for i in range(0,4):
    for j in range(0,4):
        if j==i:
            matriz[i][j]=secundario[i]
for i in range(0,4):
    for j in range(0,4):
        if j+i==3:
            matriz[i][j]=principal[i]


print 'Matriz modificada'
print ''
for i in range(0,4):
    print matriz[i]
print ''
