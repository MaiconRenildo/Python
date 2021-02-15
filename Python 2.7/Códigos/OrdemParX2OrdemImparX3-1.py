#Fazer um programa para ler dados para um vetor. Criar um outro vetor onde
#os elementos de ordem par são multiplicados por 2 e os de ordem ímpar
#multiplicados por 3 e diminuídos de 1. No final imprimir os dois vetores

tamanho=int(input('Informe a quantidade de dados que serao inseridos: '))
vetor1=[0.0]*tamanho
vetor2=[0.0]*tamanho
for i in range(0,tamanho):
    vetor1[i]=int(input('Informe o valor: '))
    if i%2==0:
        vetor2[i]=vetor1[i]*2
    else:
        vetor2[i]=(vetor1[i]*3)-1
print vetor1
print vetor2
