n=input('Informe o valor de n: ')
soma=0
i=1
while i<n:
    if n%i==0:
        soma+=i
    i+=1
if soma==n:
    print 'Eh perfeito'
else:
    print 'Nao eh perfeito'
