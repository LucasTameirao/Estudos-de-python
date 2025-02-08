# melhore o exercício 56, perguntando para o usuário se ele quer mostrar mais quantos termos, e então mostrá-los
# o programa encerra quando o usuário pedir 0 termos

primeiroTermo = int(input('digite o primeiro termo da PA >>> '))

termo = 0

r = int(input('digite a razão da PA >>> '))

c = 1

adicionarTermos = 10

print(primeiroTermo)

while adicionarTermos != 0:
    while c < adicionarTermos:
        
        termo = primeiroTermo + (r * c)
        print(termo)
        c += 1
    adicionarTermos = int(input('quantos termos a mais você deseja adicionar a PA >>> '))
    if adicionarTermos == 0:
        adicionarTermos = 0
    else:
        adicionarTermos += 1
    primeiroTermo = termo
    c = 1
print('fim do programa')