#desenvolva um programa que leia 6 números inteiros e mostre a soma apenas dos números que forem pares

print(f"-=" * 69)

s = 0

for t in range(0, 6):

    num = int(input('digite um número inteiro >>> '))
    if num % 2 == 0:
        s += num

print(f"a soma de todos os números pares que você digitou é >>> {s}")

print(f"-=" * 69)
