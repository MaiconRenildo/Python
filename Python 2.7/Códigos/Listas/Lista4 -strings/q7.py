#Faça um programa que leia uma string e crie uma outra string invertendo
#as posições de dois em dois
#Ex:  mexico => emixoc

string=raw_input('Entre com a string: ')
final=''
i=0
tamanho=len(string)
while i<(tamanho-1):
    seg=string[i]
    pri=string[i+1]
    final+=pri+seg
    i+=2
if tamanho%2!=0:
    final+=string[tamanho-1]
print final
