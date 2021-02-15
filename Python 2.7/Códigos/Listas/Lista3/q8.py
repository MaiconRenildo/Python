a=int(input('Entre com o valor de a: '))
b=int(input('Entre com o valor de b: '))
soma=0
if a>b:
    print 'A soma nao sera efetuada'
else:
    i=a+1
    while i<b:
        if i%4==0:
            soma+=i
        i=i+1
print 'A soma dos multiplos de 4 eh: ',soma
