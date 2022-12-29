class Banco:
    def __init__(self, nome, banco, conta, saldo):
        self.nome = nome
        self.banco = banco
        self.conta = conta
        self.saldo = saldo

    def mandouPix(self, valor):
        return self.saldo - valor

    def receberPix(self, valor):
        return self.saldo + valor


banco1 = Banco('Paulo Roberto', 'banco do Brasil', '111', 2500)
banco2 = Banco('Rafael Pereira', 'banco Itau', '112', 3000)
banco3 = Banco('Monica Santos', 'banco do Bradesco', '113', 5000)

n1 = float(input('Qual valor do pix você quer mandar -->'))
print(f'O cliente {banco1.nome} tinha no seu saldo --> {banco1.saldo}')
print(f'Mandou um Pix de {n1} agora seu saldo é --> {banco1.mandouPix(n1)} ')


print(banco3.receberPix(1000))
