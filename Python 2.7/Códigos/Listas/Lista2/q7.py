salario1=input('Escreva o salario do primeiro professor: ')
horas1=input('Informe as horas trabalhadas pelo primeiro professor: ')
salario2=input('Escreva o salario do segundo professor: ')
horas2=input('Informe as horas trabalhadas pelo segundo professor: ')
salarioTotal1=horas1*salario1
salarioTotal2=horas2*salario2
if salarioTotal1>salarioTotal2:
    print 'O primeiro professor tem salario maior'
else:
    print 'O segundo professor tem salario maior'
