#Digite um número e imprima a sua tabuada

num = int(input("Digite um número: "))

print(f"tabuada do número {num}:\n")

for t in range(1, 11):
    number = t * num
    print(f'{num} * {t} = {number}')
print("="*20, "Fim do programa", "="*20)