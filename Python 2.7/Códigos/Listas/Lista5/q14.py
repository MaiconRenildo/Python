#Leia uma string e imprima se ela � um palindromo. Um palindromo � uma
#cadeia que pode ser lida de frente para tr�s e de tr�s para frente.
#Ex: �SOMOS�    �1234321�

string=raw_input('Entre com a string: ')
tamanho=len(string)
palindromo=True
for i in range(tamanho//2):
    if string[i]!=string[tamanho-1-i]:
        palindromo=False
if palindromo==False:
    print 'Nao eh palindromo'
else:
    print 'Eh palindromo'
