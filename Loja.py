
def SenhaFun():
    while True:
        Senha = int(input(f'FUNCIONARIO {Nome} DIGITE SUA SENHA --> '))
        if Senha == 1234:
            break


Nome = input('QUAL E SEU NOME FUNCIONARIO --> ')
SenhaFun()
print('')
print('###  ENTRADA E SAIDA DE MERCADORIA DA LOJA  ###')
print('         ESTOQUE DE CAMISA E BERMUDAS')
print('')
Pro1 = input(f'{Nome}, QUAL MERCADORIA ENTROU NA LOJA --> ')
print(f'FUCIONARIO {Nome} ESTROU CAIXAS DE {Pro1} OU FOI POR UNIDADE')
print('')
CaixUnid = int(input(f'SE ENTRO CAIXA DE {Pro1} DIGITE [1] SE ENTRO A UNIDADE DIGITE [2] --> '))

if CaixUnid == 1:
    Quant1 = int(input(f'QUANTAS UNIDADE DE {Pro1} ENTRO NO ESTOQUE --> '))
