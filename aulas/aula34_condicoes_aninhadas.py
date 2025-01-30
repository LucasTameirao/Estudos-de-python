#Crie um programa que leia duas notas de um aluno a calcule a sua média, mostrando uma mensagem no final:
# média abaixo de 5.0: reprovado
# média entre de 5.0 e 7.0: recuperação
# média acima de 7.0: aprovado


nota = list()

for t in range(0, 2):
    x = float(input("Digite a nota do aluno >>> "))
    nota.append(x)

media = (nota[0] + nota[1]) / 2

print(f"-=" * 69)

print(f"média do aluno: {media}")

if media <= 5:
    print("aluno reprovado")
elif media <= 7:
    print("aluno em recuperação")
else:
    print("aluno aprovado")