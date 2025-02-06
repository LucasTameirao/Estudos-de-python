#crie um programa que identifique se uma palavra é, ou não, um palíndromo.

palavra = input('digite uma palavra: ')

print('palavra:\n' + palavra[::-1].replace(" ", "")) #[::-1] siginifica que a string será lida de tras para frente, INCLUINDO ESPAÇO
#replace() é um método que substitui qualquer caractere de uma string por outro caractere, nesse caso subtitui espaços por vazio.

print("--------")

if palavra[::-1].replace(" ","") == palavra.replace(' ', ''):
    print('essa palavra é um palíndromo')
else:
    print('essa palavra não é um palíndromo')