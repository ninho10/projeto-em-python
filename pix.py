class Banco:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def mandouPix(self, valor):
        return self.saldo - valor


banco1 = Banco('Paulo', 2000)
banco2 = Banco('rafael', 3000)

n1 = float(input('Qual valor do pix você quer mandar -->'))
print(f'O cliente {banco1.nome} tinha no seu saldo --> {banco1.saldo}')
print(f'Mandou um Pix de {n1} agora seu saldo é --> {banco1.mandouPix(n1)} ')
