class Conta:
    def __init__(self, titular, saldo, senha=123):
        self.titular = titular
        self.saldo = saldo
        self.senha = senha

    def extrato(self):
        sen = int(input('Digite a senha para ver o Saldo: '))
        if sen == self.senha:
            print(f'Titular: {self.titular} \nSaldo: {self.saldo}')
        else:
            print('Senha incorreta!')

    def depositar(self, deposito):
        deposito = float(input(f'Qual o valor do Deposito: '))
        self.saldo += deposito
