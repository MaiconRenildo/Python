print 'Entre com os valores'
n1=input('Primeiro numero: ')
n2=input('Segundo numero: ')
n3=input('Terceiro numero: ')
if n1<n2 and n1<n3:
    primeiro=n1
    if n2<n3:
        segundo=n2
        terceiro=n3
    else:
        segundo=n3
        terceiro=n2
else:
    if n2<n1 and n2<n3:
        primeiro=n2
        if n1<n3:
            segundo=n1
            terceiro=n3
        else:
            segundo=n3
            terceiro=n1
    else:
        primeiro=n3
        if n1<n2:
            segundo=n1
            terceiro=n2
print ''
print 'Numeros em ordem crescente: ',primeiro, segundo, terceiro
        
            
