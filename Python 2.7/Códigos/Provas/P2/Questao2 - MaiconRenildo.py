#Maicon Renildo da Silva
a=raw_input('Entre com a string: ')
tamA=len(a)
b=''
i=0
while i<tamA:
    if tamA%2==0:
        if i%2 == 0:
            b = b+a[i]
        else:
            b = b+a[tamA-i]
    else:
        if i%2 == 0:
            b = b+a[i]
        else:
            b= b+a[tamA-i-1]
    i+=1
print 'A string inicial era: ',a
print 'A estring resultante eh: ',b
    



