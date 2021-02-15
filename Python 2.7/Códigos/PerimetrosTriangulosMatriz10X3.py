#Leia uma matriz 10x3 onde cada linha corresponde aos lados de um triangulo.
#Guarde em um vetor os perimetros dos retangulos. Imprima a matriz e
#o vetor.

matriz=[]
perimetros=[]
for i in range(0,10):
    matriz.append(0)
    matriz[i]=[]
    for j in range(0,3):
        matriz[i].append(input('Informe o valor: '))
        
print ''
for i in range(0,10):
    print matriz[i]
print ''


for i in range(0,10):
    soma=0
    for j in range(0,3):
      soma+=matriz[i][j]

    perimetros.append(soma)
print perimetros
