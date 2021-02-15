#Faça um programa que leia uma string e diga se ela é um palíndromo.
#Ex: SOMOS → é palíndromo pois ela é igual sendo lida da direita
#para esquerda e da esquerda para a direita
#Ex: 123321

palin = True
cad = raw_input("entre com cadeia: ")
for i in range(0,len(cad)//2):
    if cad[i] != cad[len(cad)- i -1]:
        palin = False
if palin:
    print cad, " eh palindromo"
else:
    print cad, " nao eh palindromo"
