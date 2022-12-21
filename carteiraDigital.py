class Carteira:
    def __init__(self, nome, banco, carteira):
        self.nome = nome
        self.banco = banco
        self.carteira = carteira


n1 = None
n1 = input('Seu nome --> ')
b1 = float(input('Qual e seu saldo bancario ? --> '))
c1 = float(input('Quanto tem na sua carteira ? --> '))

carteira1 = Carteira(n1, b1, c1)

total = (carteira1.banco + carteira1.carteira)

print(f'{carteira1.nome} seja bem vido a carteira digital ')
print(f'seu saldo no banco e de {carteira1.banco}')
print(f' seu saldo na carteira e de {carteira1.carteira} ')
print(f'{carteira1.nome} seu valor total em dinheiro e {total}')
