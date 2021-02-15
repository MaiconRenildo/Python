empregados=input('Informe o numero de empregados: ')
salarioMin=input('Informe o salario minimo: ')
vendas=input("Informe o valor das vendas: ")
parte=float(vendas)/empregados
print parte
comissao=parte*0.05
salarioFinal=salarioMin+comissao
print 'O salario final de cada funcionario eh: ',salarioFinal

