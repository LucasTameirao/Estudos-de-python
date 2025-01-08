x = "12"
x = "12.5"
x = "nome"
x = True

veiculos = ["carro", "moto", "lancha", "busao"] # list / array

tupla = ("carro", "moto", "lancha", "busao") #tupla, tem seus valores inalteraveis

numbers = range(10, 300, 3) #range

dictionary = { #dict
    1: "um",
    2: "dois",
    3: "três"
}

set = {1, 1, 1, 2, 4, 4, 6, 7, 8, 8}



print(len(numbers))

for number in numbers:
    print(number)

CONST = 3,1415

# tupla(0) = "moto"// NAO PODE ALTERAR/EDITAR OS VALORES DO ARRAY

print("valor: "  + str(x))
print("tipo: " + str(type(x)))


print("valor: " + str(dictionary[1])) #vai imprimir o valor presente na chave especificada
print("tipo: " + str(type(dictionary)))

print("valor: " + str((set)))
      
print("tipo: " + str(type(set)))