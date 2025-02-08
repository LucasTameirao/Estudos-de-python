#Crie um programa que leia o ano de nascimento de 7 pessoas, no final, mostre quantas pessoas
#atingiram a maioridade e quantos não atingiram. Considere maioridade 21 anos

print(f"-=" * 69)

maiordidade = 0
menoridade = 0

for i in range(0, 7):
    idade = 0
    idade = int(input('digite a idade da pessoa >>> ')) #entrada da idade das pessoas

    if idade >= 21: #condição que analisa quantas pessoas são maiores e menores de idade
        maiordidade += 1
    else:
        menoridade += 1

print('contagem de pessoa')

print(f'{maiordidade} pessoas são maiores de idade')
print(f'{menoridade} pessoas são menores de idade')

print(f"-=" * 69)