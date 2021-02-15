#Leia dois vetores de 10 posições cada. Armazene em um vetor de 20 posições
#os elementos do vetor 1 depois os elementos do vetor 2. No final imprima
#os três vetores.

vetor1=[]
vetor2=[]
vetor3=[]

print 'Vetor 1: '
for i in range(0,10):
    vetor1.append(input('Informe o valor: '))
print 'Vetor 2: '
for i in range(0,10):
    vetor2.append(input('Informe o valor: '))
for i in range(0,10):
    vetor3.append(vetor1[i])
for i in range(0,10):
    vetor3.append(vetor2[i])
print vetor1
print vetor2
print vetor3

