#Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será a base de conversão
"""
. 1 binario
. 2 octal
. 3 hexadecimal
"""

num = int(input("Digite um número para ser convertido >>> "))

print(f"Você pode converter o número {num} para:\n. Binário [1]\n. Octal [2]\n. Exadecimal [3]")

opcao = int(input("Escolha uma opção >>> "))

if opcao == 1:
    print(f"{num} foi convertido para {bin(num) [2:]}") #função bin(), coverte um número para binário
elif opcao == 2:
    print(f"{oct(num) [2:]}") #função oct(), coverte um número para octal
elif opcao == 3:
    print(f'{hex(num) [2:]}') #função hex(), coverte um número para hexadecimal
else:
    print("voce digitou uma opção inválida") 