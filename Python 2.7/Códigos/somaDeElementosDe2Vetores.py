#Leia dois vetores de 15 posições cada, imprimir a soma dos elementos dos
#vetores e a diferença dos elementos dos vetores

vetor1=[]
vetor2=[]
s1=s2=0
print 'Vetor 1'
for i in range(0,5):
    vetor1.append(input('Informe o valor: '))
    s1+=vetor1[i]
print 'Vetor 2'
for i in range(0,5):
    vetor2.append(input('Informe o valor: '))
    s2+=vetor2[i]
st=s1+s2
dt=s1-s2
print 'Soma dos elementos dos vetores: ',st
print 'Diferenca dos elementos do vetores: ',dt

