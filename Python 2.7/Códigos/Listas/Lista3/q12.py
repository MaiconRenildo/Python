print 'Lista de alunos da professora de Geografia'
mediaT1=mediaT2=mediaT3=mediaT4=mediaT5=mediaT6=mediaT7=mediaT8=0
notat1=notat2=notat3=notat4=notat5=notat6=notat7=notat8=0

for i in range(1,241):
    turma=raw_input('Professora, informe a turma do aluno: ')
    nome=raw_input('Nome do aluno: ')
    n1=input('Nota 1: ')
    n2=input('Nota 2: ')
    media=((n1+n2)/float(2))
    if turma=='T1':
        notat1+=media
    elif turma=='T2':
        notat2+=media
    elif turma=='T3':
        notat3+=media    
    elif turma=='T4':
        notat4+=media      
    elif turma=='T5':
        notat5+=media        
    elif turma=='T6':
        notat6+=media        
    elif turma=='T7':
        notat7+=media     
    elif turma=='T8':
        notat8+=media  
    if media>=7:
        print'Aprovado'
    else:
        print 'Reprovado'

print 'Media da turma 1: ',notat1/30
print 'Media da turma 2: ',notat2/30
print 'Media da turma 3: ',notat3/3
print 'Media da turma 4: ',notat4/30
print 'Media da turma 5: ',notat5/30
print 'Media da turma 6: ',notat6/30
print 'Media da turma 7: ',notat7/30
print 'Media da turma 8: ',notat8/30



