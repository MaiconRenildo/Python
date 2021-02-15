#Maicon Renildo da Silva 19/11/2020
#Questao 2

frase=raw_input('Digite a frase: ')
tamanho=len(frase)
i=0
palavra=''
palavras=[]
while i<tamanho:
    if frase[i]!=' ':
        palavra=palavra+frase[i]
    else:
        if palavra!='':
            palavras.append(palavra)
            palavra=''
    i+=1
if palavra!='':
    palavras.append(palavra)
print 'Palavras desordenadas: ',palavras

i=0
while i<len(palavras)-1:
   j=i+1
   while j<len(palavras):
       if palavras[i]>palavras[j]:
           aux=palavras[i]
           palavras[i]=palavras[j]
           palavras[j]=aux
       j+=1
   i+=1
print 'Palavras ordenadas: ',palavras
