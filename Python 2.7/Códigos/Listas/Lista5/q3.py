#Leia um vetor de 16 posições e troque as 8 primeiras posições pelas 8
#últimas posições. Imprima o vetor original e o vetor trocado

vetorInicial=[]
vetorAux=[]
vetorFinal=[]
for i in range(0,16):
    vetorInicial.append(input('Informe um valor: '))
print vetorInicial

for i in range(0,16):
    vetorFinal.append(vetorInicial[15-i])
print vetorFinal

