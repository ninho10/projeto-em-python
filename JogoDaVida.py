print('    ####   SEJA BEM VINDO AO JOGO DA VIDA   ####')
print('')
Nome = input(' Jogador Qual è sua Nome? --> ')
AnoNasci = int(input(' Jogador {} que Ano você naisceu? --> '.format(Nome)))
AnoAtual = int(input(' Jogador {} que Ano estamos ?--> '.format(Nome)))
print('')
Idade = AnoAtual - AnoNasci
print('Jogador {}, Você tem {} ou vai fazer? '.format(Nome, Idade))
