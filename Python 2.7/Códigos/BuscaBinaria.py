#BUSCA BINARIA
array=[]
tamanho=int(input('Informe o tamanho do Array: '))
for i in range(0,tamanho):
    valor=input('Entre com o valor: ')
    array.append(valor)
array.sort()
print 'Array ordenado: ',array
procurado=int(input('Informe o valor que voce deseja procurar: '))
achou=False
fim=tamanho-1
i=0
pos=0
while i<tamanho and achou==False:
    metade=(i+fim)//2
    if array[metade]==procurado:
        achou=True
        pos=metade
    else:
        if procurado<array[metade]:
            fim=metade-1
        elif procurado>array[metade]:
            i=metade+1

if achou==True:
    print 'O numero foi encontrado na posicao: ',pos
else:
    print 'Numero nao encontrado'

    
