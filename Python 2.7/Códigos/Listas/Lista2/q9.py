gancho=input('Informe o numero de votos do capit�o gancho: ')
peter=input('Informe o numero de votos do Peter Pan: ')
wendy=input('Informe o numero de votos da Wendy: ')
total=gancho+wendy+peter
if gancho>=total/float(2):
    print 'O Capit�o Gancho foi eleito'
elif peter>=total/float(2):
    print 'O Peter Pan foi eleito'
elif wendy>=total/float(2):
    print 'A Wendy foi eleita'
else:
    print 'Segundo turno'
