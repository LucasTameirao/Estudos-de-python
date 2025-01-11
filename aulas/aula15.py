#faça um algoritmo que leia o salario de funcionario e mostre seu novo salario, com 15% de aumento.

SalarioAtual = int(input("Digite o seu salário atual >>> "))
SalarioAumento = SalarioAtual + (SalarioAtual * (15/100))

print (f"Salário atual --- R${SalarioAtual}\nSalário pós aumento de 15% --- R${SalarioAumento}")