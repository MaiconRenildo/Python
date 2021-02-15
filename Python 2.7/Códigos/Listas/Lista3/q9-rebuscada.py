numeroQuartos=input('Informe a quantidade de quartos: ')
i=1
totalQuarto=0
while i<=numeroQuartos:
    compQuarto=input('Informe o comprimento do quarto: ')
    largQuarto=input('Informe a largura do quarto: ')
    areaQuarto=compQuarto*largQuarto
    totalQuarto+=areaQuarto
    i+=1

numeroBanheiros=input('Informe a quantidade de banheiros: ')
j=1
totalBanheiro=0
while j<=numeroBanheiros:
    compBanheiro=input('Informe o comprimento do banheiro: ')
    largBanheiro=input('Informe o comprimento do banheiro: ')
    areaBanheiro=compBanheiro*largBanheiro
    totalBanheiro+=areaBanheiro
    j+=1
    
compSala=input('Informe o comprimento da sala: ')
largSala=input('Informe a largura da sala: ')
areaSala=compSala*largSala

compCozinha=input('Informe o comprimento da cozinha: ')
largCozinha=input('Informe a largura da cozinha: ')
areaCozinha=compCozinha*largCozinha

areaCasa=totalBanheiro+totalQuarto+areaSala+areaCozinha
print 'A area total da casa eh de',areaCasa,'Metros'
