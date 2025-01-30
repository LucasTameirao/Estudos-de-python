#Criar um programa simples: jogo de jokenpô (pedra, papel ou tesoura)

import random

print(f"-=" * 69)

print("vamos jogar pedra papel e tesoura, meu amigão, não será difícil.... porém será apostando algo de valor")

playerUm = input("digite: pedra, papel ou tesoura >>> ")

bot = random.randrange(1, 4)

if bot == 1:
    bot = "pedra"
elif bot == 2:
    bot = "papel"
else:
    bot = "tesoura"

print(f"dealer jogou {bot}")

if playerUm == "pedra" and bot == "tesoura" or playerUm == "papel" and bot == "pedra" or playerUm == "tesoura" and bot == "papel":
    print("Parabéns, você me derrotou pegue a sua recompensa! --- ")
elif playerUm == "pedra" and bot == "pedra" or playerUm == "papel" and bot == "papel" or playerUm == "tesoura" and bot == "tesoura":
    print("você teve sorte, tivemos um empate")
else:
    print("Pois é, esse é o jogo... e você perdeu, agora está na hora de eu pegar minha recompensa... sua alma é minha")

print(f"-=" * 69)