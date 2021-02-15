#Considere um vetor de trajetórias de 9 elementos onde cada elemento possui
#o valor do próximo elemento a ser lido.
#	Indice:  1    2    3     4    5   6    7    8    9   
#	Valor:   5    7    6     9    2   8    4    0    3
#	Fazer um programa que leia esse vetor e imprima a trajetória
#correta: sequência de impressão 5, 2, 7, 4, 9, 3, 6, 8, 0

vetor=['',5,7,6,9,2,8,4,0,3]
print vetor
valor=1
for i in range(1,10):
    print vetor[valor]
    valor=vetor[valor]
