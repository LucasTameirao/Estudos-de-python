#faça um programa que calcule a soma de todos os números ímpares que são mútiplos de 3 e que estejam
#numa sequencia de 1 a 500
print(f"-=" * 69)


print('numa sequencia de 1 a 500')

s = 0

for t in range(1, 501):
    if t % 3 == 0 and t % 2 != 0:
        s += t

print(f'o somatório de todos os números ímpares, múltiplos de 3 é >>> {s}')

print(f"-=" * 69)
