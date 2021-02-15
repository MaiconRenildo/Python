#Numero primo eh todo aquele q possui apenas dois divisores
n=input('Entre com o valor de n: ')
divisores=0
i=1
while i<=n: #E NECESSARIO TER O IGUAL
    if n%i==0:
        divisores+=1
    i+=1
    
if divisores==2:
    print 'eh primo'
else:
    print 'nao eh primo'
