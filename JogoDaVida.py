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
