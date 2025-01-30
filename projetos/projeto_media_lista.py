#Código para consulta: calculo de media de valores presentes em uma lista

import random

def calcularMedia(qtdeNumeros):

    media = list()

    for t in range(0, qtdeNumeros):
        media.append(random.randrange(0, 100))

    val = 0

    for t in range(0, len(media)):
        val += media[t]


    print(f"valores dentro da lista >>> {media}")

    print(f"somatorio de todos os valores da lista >>> {val}")

    mediaTotal = val / len(media)

    print(f"a media dos valores da lista >>> {mediaTotal}")

calcularMedia(5)