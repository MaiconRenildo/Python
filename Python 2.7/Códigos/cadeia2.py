#Faça um programa que leia duas strings e imprima a interseção
#entre as strings
#Ex:   cabelo e pelo => e, l, o

cad1 = raw_input("entre com cadeia1:")
cad2 = raw_input("entre com cadeia2:")

for i in range(0,len(cad1)):
    for j in range(0,len(cad2)):
        if cad1[i] == cad2[j]:
            print " - ", cad1[i],
