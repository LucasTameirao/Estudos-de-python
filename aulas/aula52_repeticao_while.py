#faça um programa que leia o sexo de uma pessoa, mas só aceite, 'M' OU 'F'. Caso esteja errado
#peça a digitação novamente até que esteja correto

repete = 's'
while repete == 's':
    sexo = input('Digite o seu sexo >>> ')
    sexo = sexo.upper()

    if sexo == 'F' or sexo == 'M':
        repete = 'n'

print('fim do programa')