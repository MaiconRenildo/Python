total=0
largura=input('Informe a largura do comodo: ')
comprimento=input('Informe o comprimento do comodo: ')
while largura>-1 and comprimento>-1:
    area=largura*comprimento
    total+=area
    largura=input('Informe a largura do comodo: ')
    comprimento=input('Informe o comprimento do comodo: ')
print'A area total eh de: ',total,'metros'
