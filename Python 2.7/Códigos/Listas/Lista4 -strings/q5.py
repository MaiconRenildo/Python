#Faça um programa que leia uma string e crie uma outra string
#repetindo os caracteres
#Ex:  carro => ccaarrrroo

string=raw_input('Entre com a string: ')
final=''
for i in range(0,len(string)):
    final+=2*string[i]
print final

