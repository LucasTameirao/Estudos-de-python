#Estudo sobre condições aninhadas em python

#if é a condição padrão no python (e qualquer outra linguagem de programação)
#elif seria o else if de python. é chamado de condição aninhada

nome = input("qual é o seu nome: ")

if nome == "lucas":
    print("que nome bonito, tenha um bom dia {}" .format(nome))
elif nome == "ana" or nome == "pedro":
    print("seu nome é bem comum no brasil {}" .format(nome))
elif nome == "Manu":
    print("olá minha linda, só queria que voxe soubesse q eu te amo muito")
else:
    print("tenha um bom dia")