#criação de funções

def cn():
    global frase
    frase = "olá mundo"
    print(frase)

# não pode ser iniciada pois a variável não é global, ela é limitada a função print(frase)
cn()

print(frase)