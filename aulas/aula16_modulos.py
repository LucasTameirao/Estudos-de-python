#Estudo de módulos em python

"""
import math importando uma biblioteca INTEIRA com fuções matemáticas em python

num = int(input("digite um numero >>> "))

raiz = math.sqrt(num)

print("a raiz de {} é {}".format(num, math.floor(raiz))) floor() arredonda o valor quebrado para baixo, ceil() para cima
"""

from math import sqrt, floor # Importando APENAS funções específicas do modulo math
import emoji

num = int(input("digite um numero >>> "))

raiz = sqrt(num) # não é preciso chamar o módulo ao importar APENAS uma função ex: math.sqrt() --- agora é apenas sqrt()

print("a raiz de {} é {}".format(num, floor(raiz)))
print(emoji.emojize(":sunglasses:", language='alias'))