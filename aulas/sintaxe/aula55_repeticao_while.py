# faça um programa que leia um número qualquer e mostre seu fatorial

num = int(input('digite um inteiro para descobrir seu fatorial >>> '))

i = num

while i > 1:
    num = num * (i - 1)
    i -= 1

print(num)