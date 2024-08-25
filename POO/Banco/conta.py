class Conta:
    def __init__(self, titular, saldo=0, senha=123):
        self.titular = titular
        self._saldo = saldo
        self._senha = senha

    def detalhar_conta(self):
        pass

    def mostrar_saldo(self):
        sen = int(input('Digite a senha para ver o Saldo: '))
        if sen == self.senha:
            print(f'Titular: {self.titular} \nSaldo: R${self._saldo}')
        else:
            print('Senha incorreta!')

    def extrato(self):
        sen = int(input('Digite a senha para imprimir o Extrato: '))
        if sen == self.senha:
            with open('C:\\Users\\cau-humberto\\Documents\\GitHub\\Teste_code\\POO\\extrato.txt', 'r') as arquivo:
                mensagem = arquivo.readlines()
            for linha in mensagem:
                print(linha.strip())
        else:
            print('Senha incorreta!')

    def depositar(self):
        deposito = float(input(f'Qual o valor do Deposito: '))
        self._saldo += deposito
        print('Deposito realizado com sucesso')

    def sacar(self):
        sacar = int(input('Digite o valor a ser sacado: '))
        if sacar > self._saldo:
            print(f'Seu Saldo é {self._saldo}, você não tem saldo suficiente para esse saque, tente um valor menor que seu saldo')
        else:
            self._saldo -=sacar

    def trocar_senha(self, senha):
        senha = int(input(f'Digite a Nova Senha: '))
        self._senha = senha
        print(f'Senha alterada com Sucesso, sua senha agora é: {self._senha}')

    def validar_senha(self, senha):
        senha = input('Digite a senha para ser validada: ')
        if self._senha == senha:
            print(f'Senha validada com Sucesso')
        print(f'Senha incorreta verifique a senha digitada e tente novamente')

    def cadastrar_conta(self, titular, saldo, senha):
        titular = input('Digite o nome do títular da conta: ')
        saldo = int(input('Digite o saldo dessa conta: '))
        senha = int(input('Digite a senha para a conta: '))
        self.titular = titular
        self._saldo = saldo
        self._senha = senha
        print('Conta cadastrada com sucesso!')
