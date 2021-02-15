a=int(input('Informe o valor de A: '))
b=int(input('Informe o valor de B: '))
if a>b:
    print 'A soma nao sera realizada,pois a eh menor que b'
else:
    soma=0
    i=a+1
    while i<b:
        soma+=i
        i+=1
print 'A soma dos numeros entre',a,'e',b,'eh: ',soma
