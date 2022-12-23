import mysql.connector


class Carteira:
    def __init__(self, nome, banco, dinheiro):
        self.nome = nome
        self.banco = banco
        self.dinheiro = dinheiro


n1 = None
n1 = input('Seu nome --> ')
b1 = input('Qual é banco ? --> ')
c1 = input(f'Quanto tem de dinheiro no {b1} ? --> ')

carteira1 = Carteira(n1, b1, c1)


print(f'{carteira1.nome} seja bem vido a carteira digital ')
print(
    f'seu banco é o {carteira1.banco} você tem {carteira1.dinheiro} reais na sua conta ')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="190548",
    database="mybanco"
)

mycursor = mydb.cursor()

sql = "INSERT INTO usuario (name, banco, valor, id) VALUES (%s, %s, %s, 0)"
val = (carteira1.nome, carteira1.banco, carteira1.dinheiro)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
