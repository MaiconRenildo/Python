
escada=input('Informe o tamanho da escada: ')
valores=[0]*escada
for i in range(0,escada):
    valores[i]=input('Informe o valor: ')

print 'Conjunto digitado: ',valores
diferencas=[]
#Pega todas as diferencas
for i in range(0,len(valores)-1):
    diferenca=valores[i+1]-valores[i]
    diferencas.append(diferenca)
print diferencas
#Remove as repetidas,resultando no numero de escadinhas
umavez=[]
for i in range(0,len(diferencas)):
    achou=False
    if i<len(diferencas)-1:
        if diferencas[i]!=diferencas[i+1]:
            umavez.append(diferencas[i])
    else:
        umavez.append(diferencas[i])
print umavez
print 'Numero de escadinhas: ',len(umavez)

matriz=[]
for i in range(0,len(umavez)):
    matriz.append(0)
    matriz[i]=[]

contador=0
for i in range(0,len(umavez)):

    j=contador
    while j<escada-1:
        if umavez[i]==valores[j+1]-valores[j]:
            matriz[i].append(valores[j])
        else:
            matriz[i].append(valores[j])
            contador=j
            j=escada
        j+=1
matriz[i].append(valores[j])
print matriz


