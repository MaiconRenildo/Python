#Fazer um programa para ler dois vetores de 10 posições e colocar
#em um outro vetor de no máximo 20 posições a união dos elementos.
#Colocar em um vetor de 10 posições a intercecção dos dois vetores

vetor1=[]
vetor2=[]
vetor3=[]
print 'Vetor 1'
for i in range(0,10):
    vetor1.append(input('Informe o valor: '))
print 'Vetor 2'
for i in range(0,10):
    vetor2.append(input('Informe o valor: '))
print vetor1
print vetor2


iguais=[]
for i in range(0,10):
    for j in range(0,10):
        if vetor1[i]==vetor2[j]:
            iguais.append(vetor1[i])
iguaisFinal=[]
for i in range(0,len(iguais)):
    j=i+1
    achou=False
    while j<len(iguais):
        if iguais[i]==iguais[j]:
            achou=True
            j=len(iguais)
        j+=1
    if achou==False:
        iguaisFinal.append(iguais[i])
print 'intersecao: '
print iguaisFinal


for i in range(0,10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

vetorFinal=[]
for i in range(0,len(vetor3)):
    j=i+1
    achou=False
    while j<len(vetor3):
        if vetor3[i]==vetor3[j]:
            achou=True
            j=len(vetor3)
        j+=1
    if achou==False:
        vetorFinal.append(vetor3[i])
print 'Uniao: '
print vetorFinal
    

    
