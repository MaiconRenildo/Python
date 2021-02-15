contador=0
i=2
while contador<4:
   j=1
   divisores=0
   while j<i:
       if i%j==0:
           divisores+=j
       j+=1
   if divisores==i:
       print i,' perfeito'
       contador+=1
   i+=1
