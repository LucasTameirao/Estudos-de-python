# crie um programa que leia varios numeros inteiros pelo teclado. O programa só
# vai parar quando o usuario digitar o valor 999, que é a condição de parada.
# No final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)

qtdeNumerosDigitados = 0
somatorio = 0

while True:
    n = float(input('Digite um número >>> '))
    if n == 999:
        break
    somatorio += n
    qtdeNumerosDigitados += 1

print(f'a quantidade de números digitados foi: {qtdeNumerosDigitados}')
print(f'o somatorio de todos os números digitados foi: {somatorio}')