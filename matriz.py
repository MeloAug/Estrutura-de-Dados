#passar por todos elementos usa o "for"
m = [[1, 2, 3   ], 
     [4, 5, 6   ], 
     [7, 8, 9   ], 
     [10, 11, 12]]

for l in range(4):
    print() #O "print" aqui faz colocar todos o numero iguais uma matriz, use se quiser
    for c in range(3):
        print(m[l][c], end=" ") #"end", é para jogar ao lado os numeros,não precisa usar se nao quiser