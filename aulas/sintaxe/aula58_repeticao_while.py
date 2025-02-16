# escreva um programa que leia um valor inteiro n e mostre os n primeiros termos da sequencia de fibonacci

c = 1

n = int(input('quantos numeros da sequencia de fibonacci você deseja ver >>> '))

primeiroValor = 0
segundoValor = 1

print(primeiroValor)
print(segundoValor)

while c < n - 1:
    c += 1
    proximoValor = primeiroValor + segundoValor
    print(proximoValor)
    primeiroValor = segundoValor
    segundoValor = proximoValor


         