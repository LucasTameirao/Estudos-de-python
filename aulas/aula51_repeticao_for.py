#desenvolva um programa que leia o nome, o sexo e idade de 4 pessoas, no final o programa de mostrar:
#. qual a idade do HOMEM mais velho
#. Qual a média de idade das pessoas
#. Quantas mulheres tem mais de 21 anos

print(f"-=" * 69)

menorIdade = 0
maiorIdade = 0
mediaIdade = 0
mulheresMaiorIdade = 0
nomeHomemMaisVelho = ''

for i in range(0, 4):
    nome = input('qual o seu nome >>> ')
    sexo = input("qual seu sexo >>> ")
    idade = int(input("qual a sua idade >>> "))

    mediaIdade += idade

    if sexo == 'homem':
        if menorIdade == 0 and maiorIdade == 0:
            menorIdade = idade
            maiorIdade = idade
        else:
            if idade < menorIdade:
                menorIdade = idade
            if idade > maiorIdade:
                maiorIdade = idade
                nomeHomemMaisVelho = nome

    if sexo == 'mulher':
        if idade > 21:
            mulheresMaiorIdade += 1
    
mediaIdade = mediaIdade / 4

print(f"a maior idade do homem mais velho é >>> {idade} e seu nome é >>> {nomeHomemMaisVelho}")
print(f'a media de idade das pessoas é >>> {mediaIdade}')
print(f'mulheres acima de 21 anos é >>> {mulheresMaiorIdade}')

print(f"-=" * 69)