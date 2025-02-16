#Faça um programa que recebe um ano e reotorna se ele é bissexto ou não

ano = int(input(f'digite um ano >>> '))

if ano % 4 == 0:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto')