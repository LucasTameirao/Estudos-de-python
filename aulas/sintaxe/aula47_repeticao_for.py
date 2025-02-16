#Faça um programa que lê um número inteiro e mostre se ele é um número primo ou não

print(f"-=" * 69)

num = int(input('digite um número inteiro >>> '))
tot = 0

for i in range(1, num + 1):
    if num % i == 0:
        tot += 1

if tot == 2:
    print('{} é um número primo'.format(num))
else:
    print('{} não é um número primo'.format(num))

print(f"-=" * 69)