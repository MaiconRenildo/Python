#Fazer um programa para ler dados para dois vetores e imprimir a
#interseção desses vetores

tamanho=int(input('Informe o tamanho dos vetores: '))
vetor1=[0.0]*tamanho
vetor2=[0.0]*tamanho
iguais=[]

print 'Dados para o vetor 1:'
for i in range(0,tamanho):
    vetor1[i]=input('Informe o numero: ')
    
print 'Dados para o vetor 2: '
for i in range(0,tamanho):
    vetor2[i]=input('Informe o numero: ')
j=0
f=0
while j<tamanho:
    i=0
    while i<tamanho:
        if vetor1[j]==vetor2[i]:
            iguais.append(vetor2[i])
            f+=1
            i=tamanho
        i+=1
    j+=1
print iguais


    
