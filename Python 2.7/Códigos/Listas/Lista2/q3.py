print 'Categorias de nadadores'
idade=input('Digite a idade: ')
if idade<5:
    print 'Categoria Baby'
elif idade<11:
    print 'Categoria Infantil'
elif idade<18:
    print 'Categoria Juvenil'
else:
    print 'Categoria Master'
