'''Faça um algoritmo que leia um número N e verifique se ele é primo.
Autor: Alexandre
Data: 8/10/2020'''

cont =0
n = input('entre com n: ')
i = 2
primo = True
while i < n and primo == True:
    if(n % i == 0):
        primo = False
    i = i + 1
        
if primo == True and n!=1:
    print n," PRIMO"
else:
    print n," NAO PRIMO"


        
    
