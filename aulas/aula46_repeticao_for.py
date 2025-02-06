#desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa PA


print('vamos calcular uma PA... ')

primeiroTermo = float(input('Digite o primeiro termo da PA >>> '))

razao = float(input("Digite a razao da PA >>> "))

print('a sua PA é: ')

for c in range(0, 10):
    print(f'{round(primeiroTermo + razao * c, 2)}')