#Crie um programa que lê um número e diga se ele é um numero impar ou par

num = int(input("Digite um número >>> "))

if (num % 2 == 0):
    print(f'{num} é par')
else:
    print(f'{num} é ímpar')