#Faça um programa em pascal para ler as notas de 100 alunos e imprimir quantos
#alunos tiraram nota abaixo da media da turma e quantos tiraram acima ou igual
#a media.
notas=[]
i=0
soma=0
while i<100:
    notas.append(input('Informe a nota: '))
    soma+=notas[i]
    i+=1
print 'Todas as notas: ',notas
media=soma/100
print 'Media das notas: ',media

abaixoMedia=0
acimaIgual=0
for i in range(0,100):
    if notas[i]<media:
        abaixoMedia+=1        
    else:
        acimaIgual+=1
print 'Quantidade de alunos acima da media ou na media: ',acimaIgual
print 'Quantidade de alunos abaixo da media: ',abaixoMedia

