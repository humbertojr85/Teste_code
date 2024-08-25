from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, titular, senha, limite, saldo=0):
        super().__init__(titular, senha, saldo)
        self.limite = limite
    
    def detalhar_conta(self):
        return f'{self.titular} {self._saldo} {self.limite}'
    
    def sacar(self, valor):
        if valor < self.Conta._saldo + self.limite:
            self.Conta._saldo -= valor
            return True
        return False