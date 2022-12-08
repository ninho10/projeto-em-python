from random import choice


def opcao_maquina():
    esc_maquina = choice(['esquerdo', 'meio', 'direito'])
    return esc_maquina


def opcao_jogador():
    esc_jogador = input(' Escolha esquerda, meio ou direita: --> ')
    return esc_jogador


def resultado():
    if (esc_maquina == esc_jogador):
        print('goleiro pegou')
    else:
        print('Gol')


print(opcao_jogador())
print(opcao_maquina())
print(resultado())
