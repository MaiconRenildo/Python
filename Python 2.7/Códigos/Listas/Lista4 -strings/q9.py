#Faça um programa que leia uma string e diga se ela é um palíndromo.

#Ex: SOMOS → é palíndromo pois ela é igual sendo lida da
#direita para esquerda e da esquerda para a direita

string=raw_input('Informe a string que sera verificada: ')
metade=len(string)//2
ultimo=len(string)-1
i=0
palindromo=True
while i<=metade:
    if string[i]!=string[ultimo-i]:
        palindromo=False
        i=metade+1
    else:
        i+=1
if palindromo:
    print 'Eh palindromo'
else:
    print 'Nao eh palindromo'

