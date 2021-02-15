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
            iguais+=a[i]
            j=tB+1
        j+=1
    i+=1
print 'Letras que se repetem:',iguais

final=''
for i in range(0,len(iguais)-1):
    repete=False
    j=i+1
    while j<len(iguais):
        if iguais[i]==iguais[j]:
            repete=True
            j=len(iguais)
        j+=1
    if repete==False:
        if final=='':
            final+=iguais[i]
        else:
            final+=','+ iguais[i]
final+=','+iguais[i+1]
print 'Final:',final
