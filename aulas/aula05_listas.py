#estudo de listas em python

#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

lista = list() # definição de uma lista

for i in range(1,6): # cração de um loop que irá receber 5 valores e armazená-los respectivamente na lista
    t = int(input("digite um valor: "))
    lista.append(t) # append() função que adiciona um novo valor a lista, sempre adicionando no último índicie lista[0, 1, 2, 3 + 4: novo valor]

print(f'a sua lista possui os valores {lista}')

    # lista.sort() -- um método que modifica a ordem da lista permanentemente, colocando seus valores em ordem crescente
listaOrdenada = sorted(lista) # a função sorted retorna uma nova lista ordenada em ordem crescente sem modificar a lista anterior

print(f'o maior valor da lista é {listaOrdenada[-1]}') # indicie [-1] significa o ÚLTIMO indicie da lista
print(f'o menor valor da lista é {listaOrdenada[0]}')

x = lista.index(listaOrdenada[0]) # método index recebe um valor específico em uma lista, caso esse valor exita na lista, ele retornará o seu indicie
y = lista.index(listaOrdenada[-1])

print(f'e seus respectivos indicies são: {x}: {listaOrdenada[0]} e {y}: {listaOrdenada[-1]}')