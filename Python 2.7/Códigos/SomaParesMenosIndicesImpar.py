#Refazer o programa para ler 10 dados para um Vetor e imprimir a soma
#dos elementos pares menos a soma dos elementos de índice ímpar

dados=[0.0]*10
pares=impares=0

for i in range(0,len(dados)):
    valor=input('Informe o valor do elemento: ')
    dados[i]=valor
    if dados[i]%2==0:
        pares+=dados[i]
    if i%2!=0:
        impares+=dados[i]

print 'A soma dos pares menos a soma dos impares resulta em: ',pares-impares

