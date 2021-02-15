#Leia um vetor gabarito de 10 posições, uma para cada uma das cinco questões
#da prova. E uma matriz 40x10, que contém as respostas dos quarenta alunos
#da turma. Guardar em um vetor as notas dos alunos da turma, sabendo que
#cada questão correta vale 1 ponto.

vetor=[]
for i in range(0,10):
    vetor.append(raw_input('Informe a resposta correta: '))
print vetor

matriz=[]
for i in range(0,5):
    matriz.append(0)
    matriz[i]=[]
    for j in range(0,10):
        matriz[i].append(raw_input('Informe a resposta do aluno: '))

for i in range(0,5):
    print matriz[i]

notas=[]
for i in range(0,5):
    soma=0
    for j in range(0,10):
        if vetor[j]==matriz[i][j]:
            soma+=1
    notas.append(soma)
print 'As respectivas notas dos alunos sao: ',notas
