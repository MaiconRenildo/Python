#Preencha um vetor de 10 posições com os primeiros 10 números impares.
#No final imprima o vetor. 

vetor=[]
i=contador=0
while contador<10:
    if i%2!=0:
        vetor.append(i)
        contador+=1
    i+=1
print vetor
