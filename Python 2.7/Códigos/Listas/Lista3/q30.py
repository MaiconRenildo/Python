contador=0
n=2
while contador<4:
    soma=0
    i=1
    while i<n:
        if n%i==0:
            soma+=i
        i+=1
    if soma==n:
        print n,'Eh perfeito'
        contador+=1
    n+=1


    
