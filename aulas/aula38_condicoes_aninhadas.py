#Elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal e condição de pagamento

"""
. a vista do dinheiro/cheque/boleto: 10% de desconto
. a vista no cartão: 5% de desconto
. em até 2x no cartão: preço normal
. acima de 2x no catã0: 20% de juros encima do preço original
"""
print(f"-=" * 69)

produto = float(input("Digite quanto vale o produto que você quer pagar >>> "))

print("Escolha uma das formas de pagamento:\nA vista no cartão (5% de desconto) [1]\nA vista no dinheiro/boleto/cheque (10% de desconto) [2]\nAté 2x sem juros [3]\nAté 12x vez com juros de 20% [4]")

escolha = int(input(">>> "))

if escolha == 1:
    produto = produto - (produto * 0.05)
    produto = round(produto, 2)
    print(f"Você irá pagar R${produto} à vista no cartão")
elif escolha == 2:
    produto = produto - (produto * 0.1)
    produto = round(produto, 2)
    print(f"Você irá pagar R${produto} à vista no dinheiro/boleto/cheque")
elif escolha == 3:
    produto = produto / 2
    produto = round(produto, 2)
    print(f"Você irá pagar 2 parcelas de R${produto} por mes")
elif escolha == 4:
    parcelas = int(input("em quantas parcelas você deseja dividir este produto >>> "))
    produto = produto / parcelas
    produto = produto + (produto * 0.2)
    produto = round(produto, 2)

    print(f"Você irá pagar {parcelas} de R${produto} por mes")

print(f"-=" * 69)
