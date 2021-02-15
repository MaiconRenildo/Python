idade=int(input('Informe a idade: '))
cont=maiorIdade=contExpecifico=0
while idade!=-1:
    if idade>maiorIdade:
        maiorIdade=idade
    cont+=1
    sexo=raw_input('Informe o sexo. Digite F ou M: ')
    corOlhos=raw_input('Informe a cor dos olhos: ')
    corCabelos=raw_input('Informe a cor do cabelo: ')
    print ''
    if sexo=='F' and (idade<=35 and idade>=18):
        if corCabelos=='Louro' and corOlhos=='Verde':
            contExpecifico+=1
    idade=input('Informe a sua idade: ')

print 'A maior idade dos habitantes eh: ',maiorIdade
print 'A porcentagem de mulheres louras de olhor verdes com idade entre 18 e 35 anos eh: ',(contExpecifico*100)/float(cont)
    
