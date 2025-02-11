import random


while True:
    while True:
        escolha = input('Vamos jogar! Você escolhe PAR ou IMPAR >>> ')
        escolha = escolha.upper()
        if escolha == 'PAR':
            break
        if escolha == 'IMPAR':
            break
    
    player = int(input('Digite um número para jogar >>> '))
    