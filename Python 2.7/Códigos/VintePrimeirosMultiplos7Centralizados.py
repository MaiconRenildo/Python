#Fazer um programa imprimir os 20 primeiros m�ltiplos de 7 com 4 espa�os.
#Al�m disso imprimir o t�tulo �MULT 7� centralizado.
print 'Mult 7'.center(80)
for i in range(0,20):
    print str(i*7).rjust(20)

