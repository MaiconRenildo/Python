#Leia uma frase e imprima as suas palavras.

frase=raw_input('Digite a frase: ')
#frase.split(' ') #Separa automaticamente, mas eu fiz na marra
tamanho=len(frase)
i=0
palavra=''
palavras=[]
while i<tamanho:
    if frase[i]!=' ':
        palavra=palavra+frase[i]
    else:
        if palavra!='':
            palavras.append(palavra)
            palavra=''
    i+=1
palavras.append(palavra)
print palavras

        

