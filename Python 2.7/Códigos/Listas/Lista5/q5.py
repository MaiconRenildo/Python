#Ler um vetor de números inteiros de 30 posições. Depois, ler um número
#inteiro X, imprimir quantas vezes o número X aparece no vetor.

vetor=[]
for i in range(0,30):
    vetor.append(input('Entre com o valor: '))
print vetor

encontrado=0
procurado=input('Informe o numero que voce deseja procurar: ')
for i in range(0,30):
    if procurado==vetor[i]:
        encontrado+=1
print 'O',procurado,'aparece ',encontrado,'vezes'
