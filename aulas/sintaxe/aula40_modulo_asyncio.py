import asyncio

#APENAS TESTES SOBRE O MÓDULO 'asyncio' em python

async def first():          #definição de uma função assíncrona
    for t in range(1, 11):
        await asyncio.sleep(1) #função de modulo asyncio para esperar 1 segundo com o código pausado
        print(t)

async def second():
    for t in range(0, 10):
        await asyncio.sleep(1)
        print(t)

async def main():
    task1 = asyncio.create_task(first()) #atribuição de uma task em uma variável, feita para executar dois códigos paralelamente
    task2 = asyncio.create_task(second())

    await task2 #executando a função dentro da variavel task, a ordem de execução é sempre alternando entre o código mais acima para o mais abaixo
    await task1

asyncio.run(main()) #função run() executa uma função assíncrona

