print 'Contas atrasadas'
salario=input('Informe o salario de Joao: ')
conta1=input('Informe o valor da primeira conta: ')
conta2=input('Informe o valor da segunda conta: ')
despesas=(conta1*1.02)+(conta2*1.02)
restante=salario-despesas

print 'Restou: ',restante
