#Maicon Renildo da Silva 19/11/2020
#Questao 1
linhas=int(input('Informe a quantidade de linhas: '))
coluna=int(input('Informe a quantidade de colunas: '))

perimetros=[0.0]*linhas
colunas=[0.0]*coluna

matriz=[]
for i in range(0,linhas):
    matriz.append(0)
    matriz[i]=[]
    for j in range(0,coluna):
        matriz[i].append(input('Informe o valor: '))
print 'Matriz: '
#imprime  a matriz
for i in range(0,linhas):
    for j in range (0,coluna):
        print "%6.2f" %matriz[i][j], 
    print
print ''


#Perimetros dos Quadrilateros:
for i in range(0,linhas):
    soma=0
    for j in range(0,coluna):
        soma+=float(matriz[i][j])
    perimetros[i]=soma
print 'Perimetros: ',perimetros

#Coluna das Matrizes:
for j in range(0,coluna):
    soma=0
    for i in range(0,linhas):
        soma+=float(matriz[i][j])
    colunas[j]=soma
print 'Soma das colunas: ',colunas
    
