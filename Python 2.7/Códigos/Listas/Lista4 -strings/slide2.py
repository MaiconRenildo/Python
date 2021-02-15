#Fazer um programa imprimir os 20 primeiros múltiplos de 7 com 4 espaços.
#Além disso imprimir o título “MULT 7” centralizado.
print 'Mult 7'.center(80)
for i in range(0,20):
    print str(i*7).rjust(20)

