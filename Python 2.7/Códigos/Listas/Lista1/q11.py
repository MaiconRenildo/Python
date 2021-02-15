print 'Equação do 2o Grau'
import math  
a=input('Entre com o valor de a: ')
b=input('Entre com o valor de b: ')
c=input('Entre com o valor de c: ')
delta=(b*b)-4*a*c

raiz=math.sqrt(delta)

r1=(-b+raiz)/(2*a)
r2=(-b-raiz)/(2*a)
print 'As raízes da equação são: ',r1,'e', r2
