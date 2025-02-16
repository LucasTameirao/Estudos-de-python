# Faça um programa que leia o ano de nascimento de alguém e informe, de acordo com a idade:
# . se ele ainda vai se alistar ao serviço militar
# . se é a hora de se alistar
# se já passou o tempo dele se alistar
# O programa também deve informar o tempo que falta ou que passou do prazo de alistamento

import datetime

print("-=" * 69)
dataNascimento = int(input("Qual o ano do seu nascimento >>> "))

idade = datetime.datetime.now()
idade = int(idade.strftime("%Y")) - dataNascimento

if idade < 18:
    print(f"Você tem {idade} anos. Faltam {18 - idade} anos para se alistar.\nAinda precisa completar 18 anos, ou estar no ano que completará 18 anos para se alistar")
elif idade == 18:
    print(f"Está no ano de você se alistar no exército brasileiro, você já tem, ou está fazendo, {idade} anos")
elif idade > 18:
    print(f"Caso você ainda não se alistou ja deveria ter se alistado há {idade - 18} anos")
    
print("-=" * 69)