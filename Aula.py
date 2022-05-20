import mysql.connector
import requests

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'bdyoutube',
)
cursor = conexao.cursor()
cursor.close()
conexao.close()

# CREATE = INSERT INTO

nome_produto = "Amantegueido"
valor = 7
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor} )'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

# READ = SELECT * FROM

comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)

# UPDATE = UPDATE SET WHERE

nome_produto = "Achocolateido"
valor = 15
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

# DELETE

nome_produto = "Achocolateido"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados