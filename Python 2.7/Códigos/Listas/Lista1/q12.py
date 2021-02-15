print 'Valor total no cofre'
real=input('Número de moedas de 1 real: ')
cen50=input('Número de moedas de 50 centavos: ')
cen25=input('Número de moedas de 25 centavos: ')
cen10=input('Número de moedas de 10 centavos: ')
cen5=input('Número de moedas de 5 centavos: ')
cen1=input('Número de moedas de 1 centavos: ')

tcen50=cen50*0.5
tcen25=cen25*0.25
tcen10=cen10*0.10
tcen5=cen5*0.05
tcen1=cen1*0.01

total=real+tcen50+tcen25+tcen10+tcen5+tcen1
print 'O total é: ',total,'Reais'
