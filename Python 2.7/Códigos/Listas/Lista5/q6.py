#Leia um vetor de 40 posições contar quantos elementos pares se encontram
#no vetor.

vetor=[]
for i in range(0,40):
    vetor.append(input('Entre com o valor: '))
contador=0
for i in range(0,40):
    if vetor[i]%2==0:
        contador+=1
print contador,'numeros pares'
