joao=0
ramalho=0
mattos=0
branco=0
nulo=0
for i in range(1,2001):
    voto=input('Informe seu voto: ')
    if voto==1:
        joao+=1
    elif voto==2:
        ramalho+=1
    elif voto==3:
        mattos+=1
    elif voto==4:
        branco+=1
    else:
        nulo+=1
print 'Total de votos de Joao: ',joao
print 'Total de votos de Ramalho: ',ramalho
print 'Total de votos de Mattos: ',mattos
print 'Total de votos em branco: ',branco
print 'Total de votos nulos: ',nulo
