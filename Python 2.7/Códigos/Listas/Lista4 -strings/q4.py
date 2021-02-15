#Faça um programa que leia uma string e um caractere e crie uma
#outra string sem o caractere lido.

string=raw_input('Entre com a string: ')
caracter=raw_input('Entre com o caracter: ')
filtrado=string.replace(caracter,'')
print filtrado
