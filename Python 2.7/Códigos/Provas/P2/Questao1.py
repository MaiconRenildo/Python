string=raw_input('Informe a string que sera verificada: ')
metade=len(string)//2
ultimo=len(string)-1
i=0
palindromo=True

stringb=''
f=0
j=3
while f<j:
    stringb=stringb+string[f]
    
    while i<=metade:
        if string[i]!=string[ultimo-i]:
            palindromo=False
            i=metade+1
        else:
            i+=1
    if palindromo:
        print string,'eh palindromo'
    else:
        print 'Nao eh palindromo'
