numero=input('Digite um numero de 4 digitos: ')
parte1=numero//100
parte2=numero%100
terceiro=parte1+parte2
final=terceiro*terceiro
if final==numero:
    print 'Obedece a caracteristica'
else:
    print 'Nao obedece'
