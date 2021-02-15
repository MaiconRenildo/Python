nomeProduto=raw_input('Escreva o nome do produto: ')
maiorPreco=0
while nomeProduto!='XXX':
    preco=float(input('Escreva o valor do produto: '))
    if maiorPreco<preco:
        maiorPreco=preco
        maisCaro=nomeProduto
    nomeProduto=raw_input('Escreva o nome do produto: ')
print 'O produto mais caro eh o ',maisCaro
