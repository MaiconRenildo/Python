contsim=contnao=contnaoMas=0
i=1
while i<=10:
    sexo=raw_input('informe o sexo: ')
    resposta=raw_input('resposta: ')
    print ''
    if resposta=='sim':
        contsim+=1
    else:
        contnao+=1
        if sexo=='M':
            contnaoMas+=1
    i+=1

print 'Numero de pessoas que responderam sim: ',contsim
print 'Numero de pessoas que responderam nao: ',contnao
print 'porcentagem dos homens que responderam nao: ',(contnaoMas*100)/float(contsim+contnao)
