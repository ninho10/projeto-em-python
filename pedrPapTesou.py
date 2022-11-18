from random import choice

jogador_vitorias = 0
maquina_vitoria = 0


def opcao_jogador():
    esc_jogador = input(f'{nome} Escolha pedra, papel  ou tesoura: --> ')
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
    print("-"*30)
    esc_jogador = opcao_jogador()
    esc_maquina = opcao_maquina()
    print("-"*30)

    if (esc_jogador == 'pedra') and (esc_maquina == 'tesoura') \
        or (esc_jogador == 'papel') and (esc_maquina == 'pedra') \
            or (esc_jogador == 'tesoura') and (esc_maquina == 'papel'):
        # jogador ganha
        print(f'Jogador escolheu {esc_jogador} e a Maquina escolheu {esc_maquina}'
              ' Resultado Voce Ganhou!')
        jogador_vitorias += 1

    elif esc_jogador == esc_maquina:
        # Emppate
        print(f'Jogador escolheu {esc_jogador} e a Maquina escolheu {esc_maquina}'
              ' Resultado : Empate!')

    else:
        # maquina ganha
        print(f'Jogador escolheu {esc_jogador} e a Maquina escolheu {esc_maquina}'
              ' Resultado Voce perdeu')
        maquina_vitoria += 1

    print("-"*30)
    print(f'Vitorias do Jogador : {jogador_vitorias}')
    print(f'Vitorias da maquina : {maquina_vitoria}')
    print("-"*30)

    esc_jogador = input(f'{nome}, quer Jogar ? --> ')
    if esc_jogador in ['sim', 'Sim', 'SIM', 's', 'S']:
        pass
    elif esc_jogador in ['nao', 'Nao', 'NAO', 'n', 'N']:
        break
