cadeia=raw_input('Informe a string: ')
tamCadeia=len(cadeia)

i=0
par=impar=''
while i<tamCadeia:
    if i%2==0:
        par=par+cadeia[i]
    else:
        impar=impar+cadeia[i]
    i+=1
imparInvertido=''
j=1
while j<=len(impar):
    imparInvertido=imparInvertido+impar[len(impar)-j]
    j+=1

f=j=h=0
final=''
while f<tamCadeia:
    if f%2==0:
        final=final+par[j]
        j+=1
    else:
        final=final+imparInvertido[h]
        h+=1
    f+=1
print 'A string original era: ',cadeia
print 'A string final eh: ',final



    



