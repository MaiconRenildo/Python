n=input('Informe o valor de n: ')
i=1
divisores=0
while i<=n:
    if n%i==0:
        divisores+=1
    i+=1
if divisores==2:
    print 'Eh primo'
else:
    print 'Nao eh primo'
