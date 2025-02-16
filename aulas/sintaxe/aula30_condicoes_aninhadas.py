"""
Escreva um programa para aprovar um emprestimo bancário para compra de uma casa. o programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
"""

salario = valorCasa = anosParaPagar = 0

salario = float(input("Digite o valor do seu salario >>> "))

valorCasa = float(input("Digite o valor da casa que deseja comprar >>> "))

anosParaPagar = float(input("Digite em quantos anos você conseguirá pagar essa casa >>> "))

print("-=" * 69)

valorPrestacao = valorCasa / (anosParaPagar * 12)

valorPrestacao = round(valorPrestacao, 2)

print(f"valor da prestação mensal da casa --- {valorPrestacao}")

if valorPrestacao > salario * 0.3:
    print(f"Desculpe, mas você não é capaz de pagar essa casa devido ao seu salário atual ser muito baixo\nA prestação mensal é maior do que 30% do seu salario")