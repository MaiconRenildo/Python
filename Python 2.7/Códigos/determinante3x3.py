m1=[]
m2=[]
l= input("qual a largura da matriz?")
a= input("qual a altura da matriz?")
for i in range(0,a):
    m1.append(0)
    m1[i] = []
    for j in range(0,l):
        m1[i].append(input("EL"))
for i in range(0, 3):
    v = 0
    m2.append(0)
    m2[i] = []
    for j in range(0, 5):
        if j == 3:
           m2[i].append(m1[i][0])
        elif j == 4:
           m2[i].append(m1[i][1])
        else:
           m2[i].append(m1[i][v])
           v += 1
somap=somas=0
for i in range(0, 5):
    if i < 3:
        somap += m2[0][i] * m2[1][i + 1] * m2[2][i + 2]
for i in range(2, 5):
    somas += m2[0][i] * m2[1][i - 1] * m2[2][i - 2]
print somap-somas