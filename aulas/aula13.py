#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

altura = float(input("Digite a altura em metros da parede: "))
largura = float(input("Digite a largura em metros da parede: "))

area = round(altura * largura)

tintaNecessaria = round(area / 2)

print(f"tinta necessaria {tintaNecessaria}L para {area}m² de parede")

