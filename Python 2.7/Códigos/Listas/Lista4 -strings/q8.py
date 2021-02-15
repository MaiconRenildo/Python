#Faça um programa que leia duas strings e imprima a interseção entre
#as strings
#Ex:   cabelo e pelo => e, l, o

a=raw_input('Entre com a string: ')
b=raw_input('Entre com a string: ')
iguais=''
tA=len(a)
tB=len(b)
i=0
while i<=tA-1:
    j=0
    while j<=tB-1:
        if a[i]==b[j]:
            if iguais=='':
                iguais+=a[i]
            else:
                iguais+=','+a[i]
            j=tB+1
        j+=1
    i+=1
print 'Letras que se repetem:',iguais


