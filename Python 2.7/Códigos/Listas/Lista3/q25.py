codigoCurso=raw_input('Insira o codigo do curso: ')
maior=total=0

while codigoCurso!='zero':
    numVagas=input('Insira o numero de vagas: ')
    candMas=input('Insira o numero de candidatos masculino: ')
    candFem=input('Insira o numero de candidatos femininos: ')
    porvaga=(candMas+candFem)/float(numVagas)
    print 'Numero de candidatos por vaga: ',porvaga
    total+=candMas+candFem
    pfem=(candFem*100)/float(candMas+candFem)
    print 'Porcentagem de candidatos do sexo feminino: ',pfem,'%',codigoCurso
    print ''
    if porvaga>maior:
        maior=porvaga
        codmaior=codigoCurso
    codigoCurso=raw_input('Insira o codigo do curso: ')
print 'Maior numero de candidatos por vaga: ',maior,'curso: ',codmaior
print 'Total de candidatos: ',total
    
