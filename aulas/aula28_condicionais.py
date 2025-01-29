#desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um trinângulo

a = float(input("Digite o comprimento da primeira reta >>> "))

b = float(input("Digite o comprimento da segunda reta >>> "))

c = float(input("Digite o comprimento da terceira reta >>> "))

if a + b > c and a + c > b and b + c > a:
    print(f"suas retas {a}, {b} e {c} podem formar um triângulo")
else:
    print(f"suas retas {a}, {b} e {c} não podem formar um triângulo")