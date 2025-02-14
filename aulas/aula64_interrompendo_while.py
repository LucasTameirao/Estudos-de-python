#Desenvolva um jogo de par ou ímpar, onde, o jogo só para quando o jogador perde o jogo

import random

venceu = 0

while True:
    while True:
        escolha = input('Vamos jogar! Você escolhe PAR ou IMPAR >>> ')
        escolha = escolha.upper()
        if escolha == 'PAR':
            break
        if escolha == 'IMPAR':
            break
    
    player = int(input('Digite um número para jogar >>> '))
    bot = random.randint(0, 100)

    print(f'eu jogo {bot}')

    soma = player + bot

    print(soma)

    if soma % 2 == 0 and escolha == 'PAR':
        print('Você ganhou!')
        venceu += 1
    elif soma % 2 != 0 and escolha == 'IMPAR':
        print('Você ganhou!')
        venceu += 1
    else:
        print('Você perdeu!')
        print(f'| venceu {venceu} jogo |')
        print('fim do jogo')
        venceu = 0
        break