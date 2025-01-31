#Faça um programa que faça uma contagem regressiva para o lançamento de fogos de artifício no ano novo

import asyncio

print(f"-=" * 69)

print('está iniciando a contagem regressiva para o ano novo:')

async def contador():
    for i in range(10, 0, -1):
        print(i)
        await asyncio.sleep(1)
    print('FELIZ ANO NOVO!!!')


asyncio.run(contador())

print(f"-=" * 69)
