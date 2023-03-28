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

    elif (escolhaMenur == '2'):
        os.system('cls')
        nomeEscola()
        print('Ària de alunos')
        loginAluno = input('Login -->')
        senhaAluno = input('Senha --> ')

        os.system('cls')
        nomeEscola()
        mudar = input(
            'Disciplina1     Disciplina2         Media          Faltas')

    else:
        os.system('cls')
        nomeEscola()
        print('Fim...')
        break
