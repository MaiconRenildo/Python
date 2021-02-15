print 'N primeiros termos de uma P.A '
primeiro=input('Entre com o primeiro termo: ')
razao=input('Entre com a razao: ')
fim=input('Informe a ultima posicao da sequencia: ')
i=primeiro
contador=1
while contador<=fim:
    print 'n',contador,'= ',i
    contador+=1
    i+=razao
