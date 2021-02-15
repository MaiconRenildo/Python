idade=input('Informe a idade: ')
cont=vinteum=soma=0
while idade!=100:
    soma+=idade
    cont+=1
    if idade<=65 and idade>=21:
        vinteum+=1
    idade=input('Informe a idade: ')
cont+=1
soma+=idade
print 'A idade media desse grupo de pessoas eh: ',soma/float(cont)
print vinteum*100/float(cont),'% das pessoas tem entre 21 e 65 anos'
