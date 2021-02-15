i=1
total=0
while i<=5:
    produto=float(input('Preco do produto: '))
    quantidade=input('Informe a quantidade: ')
    total+=(produto*quantidade)
    i+=1
print 'O total gasto pela empresa foi: ',total,'Reais'
