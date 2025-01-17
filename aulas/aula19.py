#Desafio Módulos: Faça um programa que leia um ângulo e retorne o seno, cosseno e tangente deste ângulo

import math # importa um módulo com funções matemáticas

angulo = float(input(""))
angulo = math.radians(angulo) #radians() é uma função que recebe um valor em angulo e retorna o mesmo valor em radianos

seno = round(math.sin(angulo), 2)
cosseno = round(math.cos(angulo), 2)
tangente = round(math.tan(angulo), 2)

print(f"o angulo {angulo}° possui valores:\nseno --- {seno}\ncosseno --- {cosseno}\ntangente --- {tangente}")
