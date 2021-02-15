print 'Preço de produtos: '
preco=input('Digite o preco inicial: ')
if preco<=50:
    preco=1.05*preco
elif preco<=100:
    preco=1.10*preco
else:
    preco=1.15*preco
print 'Preco final: ',preco

if preco<=80:
    print'Barato'
elif preco<=120:
    print 'Normal'
elif preco<=200:
    print 'Caro'
else:
    print 'Muito caro'
