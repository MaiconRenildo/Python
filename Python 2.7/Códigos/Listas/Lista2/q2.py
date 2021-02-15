print 'Calculadora'
soma='+'
sub='-'
mult='*'
div='/'
n1=input('Insira o primeiro valor: ')
operador=raw_input('Informe o operador: ')
n2=input('Insira o segundo valor: ')
if operador==soma:
    resultado=n1+float(n2)
elif operador==sub:
        resultado=n1-float(n2)
elif operador==mult:
        resultado=n1*float(n2)
elif operador==div:
    if n2!=0:
        resultado=n1/float(n2)
    else:
        print 'Nao eh possivel dividir por zero'
        resultado='Indeterminado'
else:
    resultado='Operador nao compativel'
print 'Resultado: ',resultado
