
from random import choice
import tkinter as tk


def resultado():
    jogador_vitorias = 0
    goleiro_maquina = 0


def opcao_maquina():
    esc_maquina = choice(['esquerdo', 'meio', 'direito'])
    return esc_maquina


def opcao_jogador():
    esc_jogador = ['esquerdo', 'meio', 'direito']
    return esc_jogador


def resultado():
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


janela = tk.Tk()
janela['bg'] = 'black'
janela.title('Penalti')
janela.geometry('250x250+500+250')

lblMesagem = tk.Label(
    text='# JOGO DE PENALTI #',
    foreground='white',
    background='blue'
)
lblMesagem.pack()
lblMesagem.grid(row=0, rowspan=1, column=2, columnspan=3)

lb1 = tk.Label(janela, text='Escolha jogador', bg='blue', fg='white')
lb1.grid(row=2, column=0)

v1 = tk.Entry(janela, width=22)
v1.grid(row=2, column=1, columnspan=4)

janela.mainloop()
