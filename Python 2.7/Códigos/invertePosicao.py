#Faça um programa que leia uma string e crie uma outra string invertendo
#as posições de dois em dois
#Ex:  mexico => emixoc   litro ==> ilrto

cad = raw_input("entre com cadeia: ")
cad2 = ""
for i in range(0,(len(cad)//2)):
    cad2 = cad2 + cad[2*i+1] + cad[2*i]
if len(cad)%2 == 1:
    cad2  = cad2 + cad[len(cad)-1]
print "cad:  ", cad
print "cad2: ", cad2
