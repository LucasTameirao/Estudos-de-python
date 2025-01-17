# Desafio Strings
# Crie um programa que lê o nome completo de uma pessoa e retorne:
# quantas letras tem o nome dela (sem contar espaços)
# o nome com todas minúscas
# o nome com todas maiúsculas 
# quantas letras tem o primeiro nome

nome = input("Digite seu nome completo >>> ")

print(f'seu nome começando com a primeira letra maiúcula --- {nome.title()}')
print(f'seu nome com todas as letras maiúculas --- {nome.upper()}')
print(f'seu nome com todas as letras minúsculas --- {nome.lower()}')

nomeSeparado = list() # define uma lista
nomeSeparado = nome.split() # split() separa todas as strings em listas ex: lucas assis... retorna nomeSeparado.split() = [lucas, assis]

print(f"você possui {len(nomeSeparado)} nomes")

qtdeLetrasPrimeiroNome = len(nomeSeparado[0]) # calcula quantas letras tem o primeiro nome que foi digitado
    
print(f'o nome {nomeSeparado[0]} (seu primeiro nome) tem {qtdeLetrasPrimeiroNome} letras')