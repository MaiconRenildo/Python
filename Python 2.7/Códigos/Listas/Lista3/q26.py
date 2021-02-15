inscricao=-1
mulher=homem=0
contHomemE=idadeHomemE=homem45=0
contMulherE=0
menorIdade=1000
while inscricao!=0:
    inscricao=input('Informe o numero de inscricao: ')
    idade=input('Informe a idade: ')
    sexo=raw_input('Informe o sexo: ')
    experiencia=raw_input('Voce tem experiencia: ')
    if sexo=='F':
        mulher+=1
        if experiencia=='sim':
            if idade<35:
                contMulherE+=1
            if idade<menorIdade:
                menorIdade=idade
                
    else:
        homem+=1
        if experiencia=='sim':
            contHomemE+=1
            idadeHomemE+=idade
        if idade>45:
            homem45+=1
idadeMediaH=idadeHomemE/float(contHomemE)
pHomem45=(homem45*100)/float(homem)

print 'idade media dos homens com experiencia: ',idadeMediaH
print 'Porcentagem dos homens com mais de 45entre o total de homens: ',pHomem45,'%'
print 'Numero de mulheres com menos de 35 com experiencia: ',contMulherE
print 'Menor idade entre as mulheres que ja tem experiencia: ',menorIdade

    
