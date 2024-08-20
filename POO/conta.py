class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def extrato(self):
        print(f'Titular: {self.titular} \nSaldo: {self.saldo}')

    def depositar(self, deposito):
        deposito = float(input(f'Qual o valor do Deposito: '))
        self.saldo += deposito
