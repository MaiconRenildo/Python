i=1
contador=1
n=input('Informe o valor de n: ')
while i<=n:
    contador+=2
    primo=True
    j=2
    while j<((contador/2)+1): 
       if contador%j==0:
            primo=False
            j=contador
       else:
            j+=1
    if primo==True:
        print contador
        i+=1
