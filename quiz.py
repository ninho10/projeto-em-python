import os
pontoUm = 0


# MEU QUIZ EM PYTHON


print(" Quiz do Paulo ")
answer_user = input("você que jogar ?  (S/N) -- > ")
print(answer_user)


if answer_user != "S":
    quit()     # para termina o porgrama
os.system('cls')

print(" Começando o jogo.....")
print("Qual e meu (nome)? \n (A) Pedro \n (B) Paulo \n (C) ninho \n ")
resposta1 = input(" Resposta : ")

if resposta1 == "B":
    print("Parabens Correto")
    pontoUm = pontoUm + 2
else:
    print("Esta Errada !")
os.system('cls')

print("Qual e minha (idade)? \n (A) 35 \n (B) 30 \n (C) 34 \n ")
resposta2 = input(" Resposta : ")

if resposta2 == "C":
    print("Parabens Correto")
    pontoUm = pontoUm + 2
else:
    print("Esta Errada !")
os.system('cls')

print("Qual Bairro eu (moro)? \n (A) Campinho \n (B) Madureira \n (C) Vila Valqueire \n ")
resposta2 = input(" Resposta : ")

if resposta2 == "A":
    print("Parabens Correto")
    pontoUm = pontoUm + 2
else:
    print("Esta Errada !")
os.system('cls')

print("Qual o Nome do meu (filho)? \n (A) Pedro \n (B) Rafael \n (C) Davi \n ")
resposta2 = input(" Resposta : ")

if resposta2 == "C":
    print("Parabens Correto")
    pontoUm = pontoUm + 2
else:
    print("Esta Errada !")
os.system('cls')

print("Qual e meu (time)? \n (A) Vasco \n (B) Flamengo \n (C) Palmeiras \n ")
resposta2 = input(" Resposta : ")

if resposta2 == "B":
    print("Parabens Correto")
    pontoUm = pontoUm + 2
else:
    print("Esta Errada !")
os.system('cls')

print(f'Parabens Você terminou o Jogo total de pontos : {pontoUm}')
print('FIM DE JOGO .....')
