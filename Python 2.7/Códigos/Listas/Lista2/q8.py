nEleitores=input('Informe o numero total de eleitores: ')
brancos=input('Informe o numero de votos em branco: ')
nulos=input('Informe o numero de votos nulos: ')
validos=input('Informe o numero de votos validos: ')

pbrancos=(float(brancos)*100)/nEleitores
pnulos=(float(nulos)*100)/nEleitores
pvalidos=(float(validos)*100)/nEleitores
print 'Votos brancos: ',pbrancos,'%'
print 'Votos nulos: ',pnulos,'%'
print 'Votos validos: ',pvalidos,'%'



