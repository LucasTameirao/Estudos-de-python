# melhore o jogo do desafio 28, mas agora o jogador deve tentar o jogo até ele acertar
# caso ele nao acerte continue rodando o programa q mostre quantas tentativas você fez até acertar

import random

repete = True

tentativas = 0

while repete:
    bot = random.randrange(1, 11)

    player = int(input('tente advinhar o número de 1 a 10 que eu estou pensando >>> '))

    tentativas += 1

    if player == bot:
        repete = False

print('Você acertou!!!')

print(f'tentativas >>> {tentativas}')