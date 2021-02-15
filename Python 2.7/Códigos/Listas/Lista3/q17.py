print 'Calculo da Area de um triangulo'
base=input('Informe o tamanho da bese do triangulo: ')
while base<=0:
    base=input('Erro! A base não pode ser menor ou igual a zero. Informe um tamanho valido: ')
altura=input('Informe a altura do trinagulo: ')
while altura<=0:
    altura=input('ERRO! A altura do triangulo não pode ser menor ou igual a zero. Informe um tamanho valido: ')
print 'A area do triangulo mede: ', (base*altura)/float(2),'metros quadrados'
