print 'Tripla Pitagórica'
m=input('Entre com o valor de m: ')
n=input('Entre com o valor de n: ')
if(m>n):
    lado1=(m*m)-(n*n)
    lado2=2*m*n
    hipotenusa=(m*m)+(n*n)
    print 'Lado1:',lado1,' lado2:',lado2,' hipotenusa:',hipotenusa
else:
    print 'Erro! M menor que n'
    
