somaTurmaA, somaTurmaB, somaTurmaC, somaTurmaD, somaTurmaE, somaTurmaF, somaTurmaG, somaTurmaH=0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
cont, contA, contB, contC, contD,contE, contF, contG, contH=0,0,0,0,0,0,0,0,0
nome = ""
nota1, nota2=0.0,0.0
turma=''
while cont<=240:
    nome= raw_input("nome: ")
    nota1= input("nota 1 ")
    nota2= input("nota 2 ")
    turma= raw_input("turma (de A a H): ")
    if turma == 'A' and contA<=30:
        contA+=1
        somaTurmaA+= nota1+nota2
        print "media do aluno: ", (nota1 + nota2) / 2
        print "media da turma: ", somaTurmaA / contA
    elif turma == 'B' and contB<=30:
        contB+=1
        somaTurmaB += nota1 + nota2
        print "media do aluno: ", (nota1 + nota2) / 2
        print "media da turma: ", somaTurmaB / contB
    elif turma == 'C' and contC<=30:
        contC+=1
        somaTurmaC += nota1 + nota2
        print "media do aluno: ", (nota1 + nota2) / 2
        print "media da turma: ", somaTurmaC / contC
    elif turma == 'D' and contD<=30:
        contD+=1
        somaTurmaD += nota1 + nota2
        print "media do aluno: ", (nota1 + nota2) / 2
        print "media da turma: ", somaTurmaD / contD
    elif turma == 'E' and contE<=30:
        contE+=1
        somaTurmaE += nota1 + nota2
        print "media do aluno: ", (nota1 + nota2) / 2
        print "media da turma: ", somaTurmaE / contE
    elif turma == 'F' and contF<=30:
        contF+=1
        somaTurmaF += nota1 + nota2
        print "media do aluno: ", (nota1 + nota2) / 2
        print "media da turma: ", somaTurmaF / contF
    elif turma == 'G' and contG<=30:
        contG+=1
        somaTurmaG += nota1 + nota2
        print "media do aluno: ", (nota1 + nota2) / 2
        print "media da turma: ", somaTurmaG / contG
    elif turma == 'H' and contH<=30:
        contH+=1
        somaTurmaH += nota1 + nota2
        print "media do aluno: ", (nota1 + nota2) / 2
        print "media da turma: ", somaTurmaH / contH
    cont+=1
    if (nota1+nota2)/2>=7:
        print "aprovado"
    else:
        print "reprovado"
