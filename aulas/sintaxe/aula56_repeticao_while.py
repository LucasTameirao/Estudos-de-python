# refaça o exercício de criar uma progressão aritmética , mostrando os 10 primeiros termos da PA
# agora usando o while

primeiroTermo = int(input('digite o primeiro termo da PA >>> '))

termo = 0

r = int(input('digite a razão da PA >>> '))

c = 1

print(primeiroTermo)

while c < 10:
    termo = primeiroTermo + (r * c)
    print(termo)
    c += 1

    adicionarTermos = 0
    