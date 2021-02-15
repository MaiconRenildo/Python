#Faça um programa para ler 50 valores de temperaturas em graus Celsius.
#Transformar essas temperaturas em Farenheit e imprimir a media das
#temperaturas em Celsius e Farenheit e quantas temperaturas ficaram
#acima da media em Farenheit.

celsius=[]
faren=[]
somaC=somaF=0
for i in range(0,5):
    celsius.append(input('Informe a temperatura em celsius: '))
    somaC+=celsius[i]
    faren.append(celsius[i]+32)
    somaF+=faren[i]
mediaC=somaC/float(len(celsius))
mediaF=somaF/float(len(faren))
print 'Media das temperaturas em celsius: ',mediaC
print 'Media das temperaturas em Farenheit: ',mediaF

acimaMedia=0
for i in range(0,5):
    if faren[i]>mediaF:
        acimaMedia+=1
print 'Temperaturas acima da media: ',acimaMedia
