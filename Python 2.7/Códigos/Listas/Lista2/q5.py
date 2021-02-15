altura=input('Entre com a altura: ')
sexo=raw_input('Digite F ou M para informar o sexo: ')
if sexo=='M' or sexo=='m':
    ideal=(72.7*altura)-58
elif sexo=='F' or sexo=='f':
    ideal=(62.1*altura)-44.7
else:
    ideal=-1
    
if ideal==-1:
    print 'Erro!'
else:
    print 'Peso ideal: ',ideal
    
