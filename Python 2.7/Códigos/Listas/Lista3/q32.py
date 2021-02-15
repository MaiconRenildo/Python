quantidade=int(input('Informe a quantidade de dinheiro a ser sacada: '))
while quantidade!=0:
    cin50=vin20=dez10=cin5=um1=0
    total=quantidade
    while total!=0:
        if total>=50:
            cin50+=1
            total=total-50
        elif total>=20:
            vin20+=1
            total=total-20
        elif total>=10:
            dez10+=1
            total=total-10
        elif total>=5:
            cin5+=1
            total=total-5
        elif total>=1:
            um1+=1
            total=total-1
    print cin50,'de 50,',vin20,'de 20,',dez10,'de 10,',cin5,'de cinco e',um1,'de um'
    print ''
    quantidade=int(input('Informe a quantidade de dinheiro a ser sacada: '))
    
