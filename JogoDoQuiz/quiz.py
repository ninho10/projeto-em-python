import os
import perguntas
import mysql.connector


pontoUm = 0


# MEU QUIZ EM PYTHON

jogador = input('Qual e seu nome Jogador --> ')
print(f" {jogador} Bem vindo ao -> Quiz do {perguntas.n1} <- ")
answer_user = input("você que jogar ?  (S/N) -- > ")
print(answer_user)


if answer_user != "S":
    quit()     # para termina o porgrama
os.system('cls')

print(" Começando o jogo.....")
print(
    f"Qual e meu (nome)? \n (A) Paulo Pedro \n (B) {perguntas.r1} \n (C) Paulo ninho \n ")
resposta1 = input(" Resposta : ")

if resposta1 == "B":
    print("Parabens Correto")
    pontoUm = pontoUm + 2
else:
    print("Esta Errada !")
os.system('cls')

print(f"Qual e minha (idade)? \n (A) 32 \n (B) 30 \n (C) {perguntas.r2} \n ")
resposta2 = input(" Resposta : ")

if resposta2 == "C":
    print("Parabens Correto")
    pontoUm = pontoUm + 2
else:
    print("Esta Errada !")
os.system('cls')

print(
    f"Qual Bairro eu (moro)? \n (A) {perguntas.r3} \n (B) Madureira \n (C) Vila Valqueire \n ")
resposta2 = input(" Resposta : ")

if resposta2 == "A":
    print("Parabens Correto")
    pontoUm = pontoUm + 2
else:
    print("Esta Errada !")
os.system('cls')

print(
    f"Qual o Nome do meu (filho)? \n (A) Pedro \n (B) Rafael \n (C) {perguntas.r4} \n ")
resposta2 = input(" Resposta : ")

if resposta2 == "C":
    print("Parabens Correto")
    pontoUm = pontoUm + 2
else:
    print("Esta Errada !")
os.system('cls')

print(
    f"Qual e meu (time)? \n (A) Vasco \n (B) {perguntas.r5} \n (C) Palmeiras \n ")
resposta2 = input(" Resposta : ")

if resposta2 == "B":
    print("Parabens Correto")
    pontoUm = pontoUm + 2
else:
    print("Esta Errada !")
os.system('cls')

print(f'Parabens Você terminou o Jogo total de pontos : {pontoUm}')
print('FIM DE JOGO .....')


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="190548",
    database="myquiz"
)

mycursor = mydb.cursor()

sql = "INSERT INTO jogo (id, nome, pontos) VALUES (0, %s, %s)"
val = (jogador, pontoUm)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
