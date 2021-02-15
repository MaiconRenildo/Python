saldo=input('Informe seu saldo: ')
if saldo<100:
    imposto=0
elif saldo<1000:
    imposto=0.01*saldo
elif saldo<10000:
    imposto=0.02*saldo
elif saldo<100000:
    imposto=0.03*saldo
else:
    imposto=0.05*saldo
if imposto==0:
    print 'Isento'
else:
    print 'Valor devido:',imposto
