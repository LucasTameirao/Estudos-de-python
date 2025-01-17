#desafio condicionais

import random

num = random.randrange(1, 6)

chute = int(input("Digite o mesmo numero que eu estou pensando: "))

if (chute == num):
    print("ACERTOU!!!")
else:
    print("ERROU!!!")

print(f"o numero certo era {num}")