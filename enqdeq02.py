from collections import deque
fila = ([10, 20, 30])
i = 0
while i < 5:
    x = int(input("Digite um valor: "))
    fila.append(x)
    i+=1

print(fila)
print("------------------------")

elementos = int(input("Quantos elementos voçê quer remover da fila? "))
for i in range(min(elementos, len(fila))):
    fila.popleft()
if not fila:
    print("Fila sem valores.")
else:
    print(fila)