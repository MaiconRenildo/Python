print 'Levantamento Prefeitura: '
contWoman=0
salWoman=0
contMan=0
salMan=0
maior30=0
idade=input('Entre com a idade: ')
while idade>-1:
    sexo=raw_input('Entre com o sexo: ')
    salario=input('Entre com o salario: ')
    if sexo=='M' or sexo=='m':
        contMan+=1
        salMan+=salario
    elif sexo=='F' or sexo=='f':
        contWoman+=1
        salWoman+=salario
    if idade<30:
        if maior30<salario:
            maior30=salario
    idade=input('Entre com a idade: ')
print ' '
if contMan!=0:
    mediaMan=salMan/float(contMan)
    print 'A media dos homens eh: ',mediaMan
if contWoman!=0:
    mediaWoman=salWoman/float(contWoman)
    print 'A media das mulheres eh: ',mediaWoman
if maior30!=0:
    print 'O maior salario entre as pessoas abaixo de 30 anos eh: ',maior30
print 'Fim do programa'

    
        
