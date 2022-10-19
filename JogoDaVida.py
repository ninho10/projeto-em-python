

def ZeroVinte():
    NumVin = 1
    Cont = 0
    while NumVin != 11:
        NumVin = int(input('digite o numero que estou pensando : '))
        Cont = Cont + 1


print('    ####   SEJA BEM VINDO AO JOGO DA VIDA   ####')
print('')
Nome = input(' Jogador Qual è sua Nome? --> ')
AnoNasci = int(input(' Jogador {} que Ano você naisceu? --> '.format(Nome)))
AnoAtual = int(input(' Jogador {} que Ano estamos ?--> '.format(Nome)))
print('')
Idade = AnoAtual - AnoNasci
print('Jogador {}, Você tem {} anos ou vai fazer? '.format(Nome, Idade))
N1 = int(input('se você tem, digite [1] se não digite [2]'))

if N1 == 1:
    print(' Como pode fazer uma festa e não me chamar, estou triste com Você {}.'.format(Nome))
else:
    print('{} estou feliz esse ano tem uma festa para eu ir rsrs. '.format(Nome))
print('')
print(' {} vou te fazer um desafio vou pensar em um numero entre 0 e 20 '.format(Nome))
ZeroVinte()
print(' Parabens  o numero que eu pensei foi o 11 ')
