#Leia uma frase e imprima o total de vogais, o total de brancos e o total
#do resto.

brancos=0
vogais=0
resto=0
frase=raw_input('Escreva a frase: ')
frase=frase.upper()
for i in range(0,len(frase)):
    if frase[i]=='A' or frase[i]=='E' or frase[i]=='I' or frase[i]=='O' or frase[i]=='U':
        vogais+=1
    elif frase[i]==' ':
        brancos+=1
    else:
        resto+=1
print 'Numero de vogais: ',vogais
print 'Total de brancos: ',brancos
print 'Resto: ',resto
        

    
