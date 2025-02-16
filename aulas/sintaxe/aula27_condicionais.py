# Escreva um programa q pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

salarioFuncionario = int(input("Olá, por favor, digite o valor do seu salário >>> "))

if salarioFuncionario > 1250:
    salarioFuncionario = salarioFuncionario + (salarioFuncionario * 0.1)
    print(f"seu salário recebeu um aumento de 10% e agora você receberá {salarioFuncionario}")
else:
    salarioFuncionario = salarioFuncionario + (salarioFuncionario * 0.15)
    print(f"seu salário recebeu um aumento de 15% e agora você receberá {salarioFuncionario}")

