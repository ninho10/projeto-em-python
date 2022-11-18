from random import choice

jogador_voce = 0
goleiro_maquina = 0


def opcao_maquina():
    esc_maquina = choice(['esquerdo', 'meio', 'direito'])
    return esc_maquina


print(opcao_maquina())
