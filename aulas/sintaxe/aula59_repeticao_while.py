# crie um programa que leia varios numeros inteiros pelo teclado.
# o programa para ao receber 999  como valor.
# no final mostre para o usuário quantos números ele digitou, e qual a soma dos numeros que ele digitou
# desconsidere o 999

somatorio = 0
num = 0
numerosDigitados = 0

while num != 999:
    num = int(input('Digite um número >>> '))
    if num != 999:
        somatorio += num
        numerosDigitados += 1

print(f'numeros digitados >>> {numerosDigitados}')
print(f'somatorio dos números digitados >>> {somatorio}')