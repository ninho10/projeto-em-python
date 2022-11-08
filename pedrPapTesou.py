from random import choice

jogador_vitorias = 0
maquina_vitoria = 0

def opcao_jogador():
    esc_jogador = input(f'{nome} Escolha Pedra, Papel  ou Tesoura: --> ')
    esc_jogador.lower()
    if esc_jogador == 'pedra':
        return esc_jogador
    elif esc_jogador == 'papel':
        return esc_jogador
    elif esc_jogador == 'tesoura':
        return esc_jogador
    else:
        print('opeção errada tente novamente !')
        opcao_jogador()


def opcao_maquina():
    esc_maquina = choice(['pedra', 'papel', 'tesoura'])
    return esc_maquina


nome = input('Qual e seu nome Jogador --> ')

while True:

    esc_jogador = opcao_jogador()
    esc_maquina = opcao_maquina()

    esc_jogador = input(f'{nome}, quer Jogar ? --> ')
    if esc_jogador in ['sim', 'Sim', 'SIM', 's', 'S']:
        pass
    elif esc_jogador in ['nao', 'Nao', 'NAO', 'n', 'N']:
        break
