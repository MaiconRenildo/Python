#Fazer um programa para ler uma STRING e imprimir o total de letras,
#o total de números e a quantidade de outros caracteres. 
letras=numeros=outros=0
a=raw_input('Digite algo: ')
for i in range(0,len(a)):
    if a[i].isalpha():
        letras+=1
    elif a[i].isdigit():
        numeros+=1
    else:
        outros+=1

print 'Total de letras: ',letras
print 'Total de numeros: ',numeros
print 'Total de outros caracteres: ',outros
        
