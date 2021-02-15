#Faça um programa que leia uma string e um caractere e diga quantas vezes
#o caractere aparece na string

string=raw_input('Entre com a string: ')
caracter=raw_input('entre com o caracter a ser verificado: ')
contador=0
for i in range(0,len(string)):
    if string[i]==caracter:
        contador+=1
print 'O caracter aparece ',contador,'vezes'
