#Fazer um programa para acrescentar um elemento no vetor se for digitado
#a letra “A”, remover se “R”, imprimir se “I” e sair se “F”.

array=[]
tamanho=input('Informe a quantida de elementos que serao adicionados: ')
for i in range(0,tamanho):
    valor=input('Informe o valor: ')
    array.append(valor)
print array


letra=raw_input('Digite uma letra(A/R/I/F): ')
letra=letra.upper()
while letra!='F':
    if letra=='I':
        print array
    elif letra=='R':
        array.pop()
        print array,'->Um elemento foi removido'
    elif letra=='A':
        valor=input('Informe um valor a ser adicionado: ')
        array.append(valor)
        print array,'->Um elemento foi adicionado'
    else:
        print 'Opcao invalida'
    letra=raw_input('Digite uma letra(A/R/I/F): ')
    letra=letra.upper()

