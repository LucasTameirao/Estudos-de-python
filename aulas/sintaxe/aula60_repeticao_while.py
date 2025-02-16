# crie um programa que leia varios numeros inteiros pelo teclado.
# no final da execução mostre a media entre todos os valores e qual o maior e o menor valor lido
# o programa deve perguntar se o usuário quer digitar mais um número

menorValor = 0
maiorValor = 0
media = 0
numerosDigitados = 0
num = 1

while num != 0:
    num = int(input('Digite um número [0 encerra o programa] >>> '))
    if num != 0:
        if menorValor == 0 and maiorValor == 0:
            menorValor = num
            maiorValor = num
        if num < menorValor:
            menorValor = num
        if num > maiorValor:
            maiorValor = num
        numerosDigitados += 1
        media += num
media = media / numerosDigitados
print(f'o menor valor é {menorValor}')
print(f'o maior valor é {maiorValor}')
print(f'a media dos numeros digitados é {round(media, 2)}')