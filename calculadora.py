import tkinter as tk
# janela
janela = tk.Tk()
janela['bg'] = 'blue'
janela.title('CALCULADORA')
janela.geometry('250x250+500+250')

lblMesagem = tk.Label(
    text='+ - CALCULADORA PYTHON X /',
    foreground='white',
    background='black'
)
lblMesagem.pack()
lblMesagem.grid(row=6, column=1, columnspan=3)
# labels
lb1 = tk.Label(janela, text='valor', bg='red', fg='white')
lb1.grid(row=0, column=0)

lb2 = tk.Label(janela, text='valor', bg='red', fg='white')
lb2.grid(row=1, column=0)

lb3 = tk.Label(janela, text='', bg='red', fg='white')
lb3.grid(row=5, column=0)

# caixa de texto
v1 = tk.Entry(janela, width=30)
v1.grid(row=0, column=1, columnspan=3)

v2 = tk.Entry(janela, width=30)
v2.grid(row=1, column=1, columnspan=3)

# Botões


def bt_1():
    lb3['text'] = float(v1.get()) + float(v2.get())


def bt_2():
    lb3['text'] = float(v1.get()) - float(v2.get())


def bt_3():
    lb3['text'] = float(v1.get()) * float(v2.get())


def bt_4():
    lb3['text'] = float(v1.get()) / float(v2.get())


bt1 = tk.Button(janela, width=5, text='+', command=bt_1)
bt1.grid(row=3, column=0)

bt2 = tk.Button(janela, width=5, text='-', command=bt_2)
bt2.grid(row=3, column=1)

bt3 = tk.Button(janela, width=5, text='x', command=bt_3)
bt3.grid(row=3, column=2)

bt4 = tk.Button(janela, width=5, text='/', command=bt_4)
bt4.grid(row=3, column=3)


janela.mainloop()
