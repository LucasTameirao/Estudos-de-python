#Desenvolva um programa que leia as duas notas de um aluno e calcule a média delas


"""
nota1 = float(input("Digite o valor da primeira nota: "))
print("=" * 20)

nota2 = float(input("Digite o valor da segunda nota: "))
print("=" * 20)

media = (nota1 + nota2) / 2

print(f'a média do aluno é {media}')
"""
#melhorando o desafio


listaNotas = []
repete = "S"
novoAluno = "S"

while(novoAluno == "S"):

    nome = input("Digite o nome do aluno: ")

    while (repete.upper() == "S"):
        nota = float(input("Digite a nota do aluno: "))
        listaNotas.append(nota)
        repete = input("deseja adicionar mais uma nota? [S] / [N]: ")
        novoAluno = "-"

    media = 0

    for n in listaNotas:
        media += n

    media = media/len(listaNotas)
    media = round(media, 2)
    repete = input("Deseja ver a média do aluno? [S] / [N]: ")
    if(repete.upper() == "S"):
        print(f"A média do aluno {nome} é: {media}")

    repete = input("Deseja registrar as notas de outro aluno? [S] / [N]: ")
    if(repete.upper() == 'S'):
        novoAluno = "S"
    else:
        novoAluno = "N"
print("="*20, "Fim do programa", "="*20)