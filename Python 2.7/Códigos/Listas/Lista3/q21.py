contP=contS=1
maiorAlt=segMaiorAlt=0
nome=''
while nome!='MARIA':
    nome=raw_input('Escreva o nome da candidata: ')
    altura=float(input('Informe a altura: '))
    print ''
    if altura>=maiorAlt:
        if altura==maiorAlt:
            contP+=1
        else:
            segMaiorAlt=maiorAlt
            contS=contP
            contP=1
            maiorAlt=altura
    elif altura>=segMaiorAlt:
        if altura ==segMaiorAlt:
            contS+=1
        else:
            contS=1
            segMaiorAlt=altura
print ''
print 'A segunda maior altura eh: ',segMaiorAlt,' e ha ',contS,'pessoas com ela'
print 'A maior altura eh : ',maiorAlt,' e ha',contP,' pessoas com ela'
