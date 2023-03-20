import os


def nomeEscola():
    print('  # ESCOLA XPTO #')


def menuPrincipal():
    print('''
               MENU:

               [1] - Ària de Professor
               [2] - Ària de alunos
               [3] - Sair

             ===================================''')


def areaProfessoar():
    print('''
               MENU:

               [1] - Ària de Professor
               [2] - Ària de alunos
               [3] - Sair

             ===================================''')


while True:
    os.system('cls')
    menuPrincipal()
    escolhaMenur = input('Escolha uma opeção ? --> ')
    if (escolhaMenur == '1'):
        os.system('cls')
        nomeEscola()
        print(' ÁRIA DO PROFESSOR')
        loginProfessor = input('Login --> ')
        senhaProfessor = input('Senha --> ')
        teste = input('..............')

    elif (escolhaMenur == '2'):
        os.system('cls')
        print('Ària de alunos')

    else:
        os.system('cls')
        nomeEscola()
        print('Fim...')
        break
