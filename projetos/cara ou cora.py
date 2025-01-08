import random

#Software para lançar uma moeda e obter seu valor: cara ou coroa

def ThrowCoin(times): #função responsavel por lançar a moeda, seu parametro define quantas moedas serão arremessadas

    coroa = 0
    cara = 0

    listTimes = range(times)

    for t in listTimes: # loop para calcular quantas moedas serão lançadas

        x = random.randrange(1, 3) # função que entrega um número aleatório, começa a partir do primeiro valor, e para um numero antes do segundo valor
        if x == 1:
            cara += 1 # contabiliza quantas caras saíram
            print("cara")
        elif x == 2:
            coroa += 1 # contabiliza quantas coroas saíram
            print("coroa")
    
    print("caíram:", coroa, "coroas e:", cara, "caras")

ThrowCoin(15000) # executa a função
