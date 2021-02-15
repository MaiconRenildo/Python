#Questao 2 - Prova 1            22/10/2020
#Maicon Renildo da Silva
n=contador=0
f=1
quantidade=input('Informe quantos numeros voce deseja verificar: ')
print ''
while f<=quantidade:
    n=input('Informe o valor de n: ')
    i=1
    while i<=n:
        triangular=False
        produto=i*(i+1)*(i+2)
        if (n==produto):
            triangular=True
            contador+=1
            i=n+1
        i+=1    
    if triangular==True:
        print n,'eh triangular'
    else:
        print n,'nao eh triangular'
    print ''
    f+=1
        
print 'Foram digitados',contador,'numeros triangulares'
            
