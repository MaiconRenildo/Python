nascidas=input('Numero de criancas nascidas do periodo: ')
sexo=''
contmorta=contMas=contMeses=0
sexo=raw_input('Sexo da crianca morta: ')
while sexo!='vazio':
    meses=input('Numero de meses de vida: ')
    contmorta+=1
    if meses<=24:
        contMeses+=1
    if sexo=='masculino':
        contMas+=1
    sexo=raw_input('Sexo da crianca morta: ')
print 'Porcentagem de crianças mortas no periodo: ',(contmorta*100)/float(nascidas),'%'
print 'Porcentagem de crianças do sexo masculino mortasno periodo: ',(contMas*100)/float(nascidas),'%'
print 'Porcentagem de crianças que viveram 24 meses ou menos: ',(contMeses*100)/float(nascidas),'%'
