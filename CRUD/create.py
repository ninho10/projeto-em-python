import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="loja",
)
cursor = conexao.cursor()

funcao = "balconista"
login_usuario = "roberto"
senha_usuario = "1010"

comando = f'INSERT INTO usuarios (funcao, login_usuario, senha_usuario) VALUES ("{funcao}", "{login_usuario}", "{senha_usuario}")'

cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
