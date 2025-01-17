#Crie um programa que pergunte a distancia em Km de uma viagem e cobre R$0,50 por Km para viagens de até 200km
#Para viagens mais longas cobre R$0,45

viagemKm = int(input('qual a distancia em Km da sua viagem: '))

if viagemKm <= 200:
    precoViagem = viagemKm * 0.50
    print(f'sua viagem vai custar R${precoViagem}')
else:
    precoViagem = viagemKm * 0.45
    print(f'sua viagem vai custar R${precoViagem}')