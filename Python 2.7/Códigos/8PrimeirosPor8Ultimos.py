#Leia um vetor de 16 posi��es e troque as 8 primeiras posi��es pelas 8
#�ltimas posi��es. Imprima o vetor original e o vetor trocado

vetorInicial=[]
vetorAux=[]
vetorFinal=[]
for i in range(0,16):
    vetorInicial.append(input('Informe um valor: '))
print vetorInicial

for i in range(0,16):
    vetorFinal.append(vetorInicial[15-i])
print vetorFinal

