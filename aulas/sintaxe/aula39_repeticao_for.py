#Estudo sobre laço de repitição for...

for i in range(0, 6): #laço for padrão, range(x, y) o primeiro argumento é o inicio da repetição, o segundo -1 é o fim da repetição
    print(i)

print("-" * 10)

for t in range(5, -1, -1): #o -1, no terceiro argumento, significa que o laço contará de tras para frente
    print(t)

n = int(input('digite um numero >>> '))

for i in range(0, n + 1):
    print(i)

n = range(0, 6)

print(n[5])

s = 0

for i in range(0, 4):
    n = int(input('digite um número >>> '))
    s += n
print(f'somatórios dos seus valores é igual a {s}')