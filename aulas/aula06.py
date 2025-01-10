#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro ele não será adicionado. No final, serão exibidos todos os valores únicos digitados
#em ordem crescente

lista = list()
valorDigitado = 0
continuar = "s"

while (continuar == "s"): #loop que irá continuar até minha condição ser falsa
    valorDigitado = int(input("Digite um valor: "))

    if(valorDigitado in lista): #condição o "in" verifica se o valor digitado existe na lista indicada, caso exista ele retornará True
        print("valor já existente, escolha outro\n" + "=" * 150)   
    else:
        lista.append(valorDigitado)

    continuar = input("Deseja continuar? [s] ou [n]: ")
    continuar = continuar.lower() #Método "lower" transforma todas os caracteres de uma string em minúsculo... Upper() em maiúsculo

lista.sort()

print(lista)
