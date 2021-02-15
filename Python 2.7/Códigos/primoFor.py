'''Faça um algoritmo que leia um número N e verifique se ele é primo.
Autor: Alexandre
Data: 8/10/2020'''

cont =0
n = input('entre com n: ')
for i in range(2,n):
    if(n%i == 0):
        cont = cont + 1
if cont == 0 and n!=1:
    print n," PRIMO"
else:
    print n," NAO PRIMO"


        
    
