n=input("Informe a posicao do ultimo valor: ")
contador=0
i=2#primeiro numero a ser analisado
while contador<=n:
   j=1 #numero verificador
   divisores=0
   while j<=i:
       if i%j==0:
           divisores+=1
       j+=1
   if divisores==2:
       contador+=1
       print contador,'o primo eh: ',i
   i+=1
