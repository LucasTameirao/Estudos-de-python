#faça um algoritmoque leia o preço de um produto e mostre seu novo preço, com 5% de desconto

nomeProduto = input("Digite o nome do produto >>> ")
precoProduto = float(input(f"Digite o preço do {nomeProduto} >>> "))
precoProdutoDesconto = precoProduto - (precoProduto * 0.15)

print(f'preço inicial --- R${precoProduto}\nvalor do desconto (15%) --- R${precoProduto * 0.15}\npreço com 15% de desconto --- R${precoProdutoDesconto}')