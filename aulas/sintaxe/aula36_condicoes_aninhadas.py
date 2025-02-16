#refaça o desafio da aula 28 dos triangulos acescentando o recurso de mostrar que tipo de triangulo sera formado

"""
equilatero: todos os lados iguais
isósceles: dois lados iguais
escaleno: todos os lados diferentes
"""
print(f"-=" * 69)

a = float(input("Digite o comprimento da primeira reta >>> "))

b = float(input("Digite o comprimento da segunda reta >>> "))

c = float(input("Digite o comprimento da terceira reta >>> "))

if a + b > c and a + c > b and b + c > a:
    print(f"suas retas {a}, {b} e {c} podem formar um triângulo") 
   
    if a == b and a == c and b == c:
        print("seu triângulo é equilátero: possui todos os lados iguais")
    elif a == b or a == c or b == c:
        print("seu triângulo é isósceles: possui dois lados iguais")
    else:
        print("seu triângulo é escaleno: possui todos os lados diferentes")
else:
    print(f"suas retas {a}, {b} e {c} não podem formar um triângulo")

print(f"-=" * 69)