#projeto de uma calculadora simples

#inicialização de variáveis:

num1 = 0
num2 = 0
operacao = 0
res = 0

num1 = float(input("\ncalculadora simples: \ndigite o primeiro valor: "))

operacao = input("\ndigite uma operação + (soma), - (subtração), * (multiplicação), / (divisão): ")

num2 = float(input("\ndigite o segundo valor: "))

def calculo():
    if(operacao == "+"):
        res = num1 + num2
        print("o resultado da operação é: ", res)
    elif(operacao == "-"):
        res = num1 - num2
        print("o resultado da operação é: ", res)
    elif(operacao == "*"):
        res = num1 * num2
        print("o resultado da operação é: ", res)
    elif(operacao == "/"):
        res = num1 / num2
        print("o resultado da operação é: ", res)

calculo()   