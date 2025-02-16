# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
"""
até 9 anos: mirim
até 14 anos: infantil
até 19 anos: junior
até 20 anos: senior
acima de 20 anos: master
"""
print(f"-=" * 69)

idade = int(input("Digite sua idade aqui >>> "))

if idade <= 9:
    print("Você está na categoria mirim (abaixo de 10 anos)")
elif idade <= 15:
    print("Você está na categoria infantil (abaixo de 16 anos)")
elif idade <= 19:
    print("Você está na categoria junior (abaixo de 20 anos)")
elif idade == 20:
    print("Você está na categoria senior (abaixo de 21 anos)")
else:
    print("Você está na categoria master (acima de 20 anos)")

print(f"-=" * 69)