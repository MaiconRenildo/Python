i=1
maior=numeroMaior=0
menor=numeroMenor=999999
while i<=5:
    peso=input('Informe o peso do boi: ')
    numero=input('Informe o numero de identificacao do boi: ')
    print ''
    if peso<=menor:
        menor=peso
        numeroDoMenor=numero
    if peso>=maior:
        maior=peso
        numeroDoMaior=numero

    i+=1
print 'O boi mais magro pesa: ',menor,'kg e eh identificado pelo numero: ',numeroDoMenor
print 'O boi mais gordo pesa: ',maior,'Kg e eh identificado pelo numero: ',numeroDoMaior
