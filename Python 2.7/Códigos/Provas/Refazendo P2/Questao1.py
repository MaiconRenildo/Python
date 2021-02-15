cadeia=raw_input('Informe a string: ')
tamCadeia=len(cadeia)
if tamCadeia<3:
    print 'String pequena demais'
else:
    a=2
    y=0
    while y<=tamCadeia-3:
        j=a+1
        while j<=tamCadeia:
            cVar=''
            f=y
            while f<j:
                cVar=cVar+cadeia[f]
                f+=1
            tamCVar=len(cVar)
            palindromo=True
            i=0
            while i<tamCVar:
                if cVar[i]!=cVar[tamCVar-1-i]:
                    palindromo=False
                    i=tamCVar
                else:
                    i+=1
            if palindromo:
                print cVar,'eh palindromo '
            j+=1
        a+=1
        y+=1

    



