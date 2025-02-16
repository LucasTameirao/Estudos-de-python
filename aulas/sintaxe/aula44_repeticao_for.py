#refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher

print(f"-=" * 69)


num = int(input('digite um número para descobrir a sua tabuada >>> '))

print(f'a tabuada de {num} é: ')

for t in range(0, 11):
    print(f'{num * t}')

print(f"-=" * 69)
