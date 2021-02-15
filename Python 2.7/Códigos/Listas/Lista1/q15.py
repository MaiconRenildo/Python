print 'Ano,meses e dias'
dias=input('Entre com o numero de dias: ')
ano=dias/365
meses=(dias%365)/30
tdias=(dias%365)%30

print ano,'anos',meses,'meses','e',tdias,'dias'
