#Maicon Renildo da Silva 19/11/2020
#Questao 3

palavras=['burro','idiota','animal','espertalhao','abc']
print 'Palavras desordenadas: ',palavras

#Metodo da bolha
tamanho=len(palavras)
i=0
while i<tamanho-1:
   j=i+1
   while j<tamanho:
       if len(palavras[i])>len(palavras[j]):
           aux=palavras[i]
           palavras[i]=palavras[j]
           palavras[j]=aux
       j+=1
   i+=1
print 'Vetor ordenado: ',palavras
