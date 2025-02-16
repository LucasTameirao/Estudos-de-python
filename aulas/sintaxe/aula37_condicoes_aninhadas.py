#desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status, de acordo
#com a tabela abaixo:

"""
. abaixo de 18.5: abaixo do peso
. entre 18.5 e 25:Peso ideal
. 25 até 30: sobrepeso
. 30 a 40: Obesidade 
. acima de 40: obesidade mórbida
"""
print(f"-=" * 69)

peso = float(input("Digite seu peso >>> "))

altura = float(input("Digite sua altura >>> "))

imc = peso / altura ** 2

print(f"seu imc é --- {round(imc, 2)}")

if imc < 18.5:
    print("Você está abaixo do peso (imc abaixo de 18.5)")
elif imc < 26:
    print("Você está no peso ideal (imc entre 18.5 e 25)")
elif imc < 31:
    print("Você está em estado de sobrepeso (imc entre 25 e 30)")
elif imc < 41:
    print("Você está em estado de obesidade (imc entre 30 e 40)")
else:
    print("Você está em estado de obesidade mórbida (acima de 40)")

print(f"-=" * 69)