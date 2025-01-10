#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode converter
#considere US$1,00 = R$3,27

dinheiroReal = float(input("digite quantos reais você possui na sua carteira: "))

dinheiroDolar = dinheiroReal / 3.27
dinheiroDolar = round(dinheiroDolar, 2)

print(f"Você pode comprar US${dinheiroDolar} com R${dinheiroReal}")
print("="*20, "Fim do programa", "="*20)