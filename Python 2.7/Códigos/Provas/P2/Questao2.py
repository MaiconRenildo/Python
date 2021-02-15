#Maicon Renildo da Silva

a=raw_input('Entre com a string: ')
i=0
par=''
impar=''
impares=''

while i<len(a):
    if i%2==0:
        par+=a[i]
    else:
        impar+=a[i]
    i+=1

tamPar=len(par)
tamImpar=len(impar)
soma=tamPar+tamImpar
j=0
resto=''
print par
print impar



    



