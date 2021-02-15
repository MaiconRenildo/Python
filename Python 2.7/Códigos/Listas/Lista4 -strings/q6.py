#Faça um programa que leia uma string e crie uma outra string
#repetindo apenas as  vogais
#Ex:  carro => caarroo

string=raw_input('Entre com a string: ')
fim=''
string=string.lower()
for i in range(0,len(string)):
    if string[i]=='a' or string[i]=='e' or string[i]=='i'\
    or string[i]=='o' or string[i]=='u':
        fim+=2*string[i]
    else:
        fim+=string[i]
print fim

