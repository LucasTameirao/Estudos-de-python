#Desafio Módulos: faça um programa que leia o comprimento dos catetos de um triagulo retângulo e retorne o comprimento
#da hipotenusa

import math

catetoOposto = float(input("Digite o comprimento do cateto oposto >>> "))
catetoAdjacente = float(input("Digite o comprimento do cateto adjacente >>> "))

hipotenusa = math.sqrt(pow(catetoAdjacente, 2) + pow(catetoOposto, 2) )

print(f"cateto adjacente --- {catetoAdjacente}m\ncateto oposto --- {catetoOposto}m\nhipotenusa --- {hipotenusa}")