#METODO DA BOLHA

tamanho=input('Informe a quantidade de numeros que deseja inserir: ')
array=[]
for i in range(0,tamanho):
    valor=input('Informe o valor: ')
    array.append(valor)
print 'Vetor inicial: ',array
i=0
while i<tamanho-1:
   j=i+1
   while j<tamanho:
       if array[i]>array[j]:
           aux=array[i]
           array[i]=array[j]
           array[j]=aux
       j+=1
   i+=1
print 'Vetor ordenado: ',array
       
