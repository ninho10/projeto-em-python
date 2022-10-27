import os

CaixUnid = 0
Caixa1 = 0
QuantCaixa1 = 0
TotalPro = 0
QuantUnidade1 = 0

def SenhaFun():
    while True:
        Senha = int(input(f'FUNCIONARIO {Nome} DIGITE SUA SENHA --> '))
        if Senha == 1234:
            break


Nome = input('QUAL E SEU NOME FUNCIONARIO --> ')
SenhaFun()
os.system('cls')
print('')
print('###  ENTRADA E SAIDA DE MERCADORIA DA LOJA  ###')
print('         ESTOQUE DE CAMISA E BERMUDAS')
print('')
Pro1 = input(f'{Nome}, QUAL MERCADORIA ENTROU NA LOJA --> ')
print(f'FUCIONARIO {Nome} ENTROU CAIXAS DE {Pro1} OU FOI POR UNIDADE')
os.system('cls')
print('')
CaixUnid = int(
    input(f'SE ENTRO CAIXA DE {Pro1} DIGITE [1] SE ENTRO A UNIDADE DIGITE [2] --> '))

if CaixUnid == 1:
    Caixa1 = int(input(f'QUANTAS CAIXAS DE {Pro1} ENTRO NO ESTOQUE --> '))
    QuantCaixa1 = int(
        input('QUAL E A QUANTIDADE DE PRODUTOS DENTRO DA CAIXA --> '))
    TotalPro = (Caixa1 * QuantCaixa1)
    print(f'O TOTAL DE {Pro1} NO ESTOQUE E : {TotalPro}')

if CaixUnid == 2:
    QuantUnidade1 = int(
        input('QUAL E A QUANTIDADE DE PRODUTOS --> '))
    print(f'O TOTAL DE {Pro1} NO ESTOQUE E : {QuantUnidade1}')
