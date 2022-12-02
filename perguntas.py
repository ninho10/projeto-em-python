import tkinter as tk


class Messagem:
    def __init__(self, saldar, idade):
        self.saldar = saldar
        self.idade = idade

    def bomDia(self):
        print(f'Pazer conhecer você, {n2}')


janela = tk.Tk()
janela['bg'] = 'black'
janela.title('NOVIDADE')
janela.geometry('300x300')

n1 = tk.Label(text='SEU NOME ?')
n1.grid(row=0, column=0)

n2 = tk.Entry()
n2.grid(row=0, column=2, columnspan=4)

n1 = tk.Label(text='SEU IDADE ?')
n1.grid(row=2, column=0)

n2 = tk.Entry()
n2.grid(row=2, column=2, columnspan=4)


janela.mainloop()
