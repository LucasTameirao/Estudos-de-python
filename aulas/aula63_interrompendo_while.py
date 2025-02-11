while True:
    numero = int(input('Digite o número que deseja consultar a tabuada >>> '))
    if numero < 0:
        print("Você finalizou o programa")
        break
    for i in range(1, 11):
        print(f'{numero} * {i} = {numero * i}')