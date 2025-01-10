#Digite um valor em metros e o converta para centimetros e milímetros

medida = 0

medida = float(input("Digite um valor de medida em metros >>> "))

medidaCm = medida * 100
medidaMm = medida * 1000

print(f"Sua medida em metros é {medida}\nEm centímetros é {medidaCm}\nEm milímetros é {medidaMm}")
print("="*20, "Fim do programa", "="*20)