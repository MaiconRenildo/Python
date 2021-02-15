hinicio=input('Informe o horario do inicio da viagem: ')
mininicio=input('Informe os minutos: ')
segundos=input('Informe os segundos: ')
totalInicio=(hinicio*3600)+(mininicio*60)+segundos

hfim=input("Informe o horario final: ")
minfim=input('Informe o minuto final: ')
segfim=input('Informe os segundos no final da viagem: ')
totalfim=(hfim*3600)+(minfim*60)+segfim

diferenca=totalfim-totalInicio

hora=diferenca//3600
minuto=(diferenca%3600)//60
segundo=(diferenca%3600)%60

print hora,':',minuto,':',segundo
