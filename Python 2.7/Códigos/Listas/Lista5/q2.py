#Ler um vetor de 12 posi��es inteiras e depois ler dois n�meros X e Y de
#1 a 12. Imprimir  soma das posi��es X e Y do vetor.
vetor=[0.0]*12
for i in range(0,12):
    vetor[i]=input('Informe o valor: ')
print vetor

x=int(input('Informe x(numero entre 1 e 12: '))
y=int(input('Informe y(numero entre 1 e 12: '))
soma=vetor[x-1]+vetor[y-1]
print 'A soma das posicoes eh: ',soma
