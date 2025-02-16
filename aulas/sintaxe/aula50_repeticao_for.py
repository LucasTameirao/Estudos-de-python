#faça um programa que leia o peso de 5 pessoas, e mostre qual o maior e o menor peso lido

print(f"-=" * 69)

menor = 0
maior = 0

for p in range(0, 5):
    peso = float(input('digite o peso da pessoa >>> '))

    if p == 0:
        menor = peso
        maior = peso
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso


print(f'o maior peso é {maior}')
print(f'o menor peso é {menor}')

print(f"-=" * 69)