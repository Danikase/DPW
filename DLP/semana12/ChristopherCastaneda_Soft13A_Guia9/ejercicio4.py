# Imprimir los multiplos del 3 que esten antes del 20

num = 0
total = 0

while num in range(0, 20):
    num += 3
    total += num
    if num == 18:
        break

print(total)