#Desafio Módulos: Crie um programa que lê um número real qualquer pelo teclado e mostre na tela
#sua porção inteira 
#Ex.: numero 5.64532 >>> 5

from math import floor

num = float(input(f"Digite um número com ponto flutuante >>> "))

print(f"o numero {num} arredondado se torna {floor(num)}") # a função floor deveria ser acessada atraves de math.floor, porém foi importada apenas a função floor