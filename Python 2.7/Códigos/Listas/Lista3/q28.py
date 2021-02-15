posicao=input('Informe a posicao do ultimo numero primo: ')
contador=0
i=1#valor a ser verificado
while contador<posicao:
    divisores=0
    j=1#valor que verifica 
    while j<=i:
        if i%j==0:
            divisores+=1
        j+=1
    if divisores==2:
        print i,'eh primo'
        contador+=1
    i+=1
