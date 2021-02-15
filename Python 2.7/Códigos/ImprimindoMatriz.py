mat = []
for i in range(0,4):
    mat.append(0)
    mat[i] = []
    for j in range(0,5):
        mat[i].append(input("entre com M1"))


#imprime  a matriz
for i in range(0,4):
    for j in range (0,5):
        print "%7.2f" %mat[i][j], #2+1(ponto)+4
    print


vet = [0]*20
for i in range(0,4):
    for j in range(0,5):
        vet[5*i+j] = mat[i][j]
print vet

# i = 0, 0 1 2 3 4,, i = 1, 5 6 7 8 9,, i = 2, 10 11 12 13 14 ...  
