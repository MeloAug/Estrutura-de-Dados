v = []
for i in range (4):
    x = int(input('digite um valor: '))
    v.append(x)
for i in range(4):
    print(v[i], end= ' ')
print()
v.pop(len(v)-1)
print(v)