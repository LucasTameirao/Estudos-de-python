import mysql.connector # pip install myslq-connector-python

# um software desenvolvido para rodar um sistema CRUD

conexao = mysql.connector.connect( # mysql.connector.connect() é o método para conectar o banco de dados ao código
    host = 'localhost',
    user='root',
    password='',
    database='sistema_crud_python'
)

cursor = conexao.cursor() # cursor() é o método que serve para executar métodos de comando para o banco de dados

# é através do cursor que eu usarei o: CREATE READ UPDATE DELETE

nome_produto = input('Digite o nome do produto que deseja adicionar >>> ')
valor = input(f'Qual o valor que você deseja dar para {nome_produto} >>> ')

#CRUD:

# CREATE:

create = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", "{valor}")' # o comando executado deve sempre ser escrito dentro de aspas simples ''

cursor.execute(create) #executa (interpreta) os comandos em MySQL

conexao.commit() # executa comandos de edição: CREATE, UPDATE, DELETE... em outras palavras e salva a tabela

print(f"{nome_produto} foi criado com sucesso")

#READ

select = 'SELECT * FROM vendas'

def Select():

    cursor.execute(select)

    resultado = cursor.fetchall() # executa o comando de leitura: READ

    return print(resultado)


Select()


#UPDATE:

nome_produto = input('qual produto você deseja alterar o valor >>> ')

valor = input("selecione o novo valor do produto >>> ")

update = f'UPDATE vendas SET valor = "{valor}" WHERE nome_produto = "{nome_produto}"'

cursor.execute(update)

conexao.commit()

print('valor alterado com sucesso')

Select()

#DELETE

nome_produto = input("digite o nome do produto que você deseja excluir >>> ")

delete = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'

cursor.execute(delete)

conexao.commit()

print(f'{nome_produto} foi deletado com sucesso')

# Só pra finalizar

Select()