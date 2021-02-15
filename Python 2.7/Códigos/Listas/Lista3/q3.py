numero=int(input('Entre com o numero: '))
pares=0
somaPar=0
impares=0
while numero!=0:
    if numero%2==0:
        somaPar+=numero
        pares+=1
    else:
        impares+=1
    numero=int(input('Entre com o numero: '))
print 'Quantidade de numeros pares: ',pares
print 'Quantidade de numero impares: ',impares
print 'Media dos numeros pares: ',somaPar/float(pares)
