#Estudo condicionais: Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custa R$7,00 por cada Km acima da velocidade limite

velCarro = 0
velCarro = int(input("quantos Km está o seu carro >>> "))

if (velCarro > 80):
    multa = 7 * (velCarro - 80)
    print(f'Seu carro foi multado, a multa custa R${multa},00')
else:
    print("seu carro não foi multado")