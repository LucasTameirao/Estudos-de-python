# Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Os dois números são iguais, não existem valor maior

print("\nVamos comparar dois números diferentes...")

print("-=" * 69)

val1 = float(input("digite um valor >>> "))

val2 = float(input("digite um segundo valor >>> "))

if val1 > val2:
    print(f"{val1} é maior que {val2}")
elif val2 > val1:
    print(f"{val2} é maior que {val1}")
else:
    print("os dois números são iguais")
    
print("-=" * 69)