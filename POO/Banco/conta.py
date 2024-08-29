from datetime import datetime


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

    def depositar(self):
        deposito = float(input(f'Qual o valor do Deposito: '))
        self._saldo += deposito
        print('Deposito realizado com sucesso')

    def sacar2(self):
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


    def sacar(self):
        valor_saque = int(input('Digite o valor a ser sacado: '))
        # Verifica se o valor do saque é válido
        if valor_saque > self._saldo:
            print("Saldo insuficiente para realizar o saque.")
            return self._saldo

        # Deduz o valor do saque do saldo
        self._saldo -= valor_saque
        
        # Obtém a data e hora atuais
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Texto a ser gravado no extrato
        registro = f"Feito em {data_hora} \nTitular: {self.titular}\nSaldo Anterior: {valor_saque + valor_saque} \nSaque: R${valor_saque:.2f} \nSaldo Atual: R${self._saldo:.2f} \n----------------------------------------------------------------\n"
        
        # Abre o arquivo extrato.txt e grava o registro
        try:
            with open('C:\\Users\\cau-humberto\\Documents\\GitHub\\Teste_code\\POO\\Banco\\extrato.txt', 'a') as arquivo:
                arquivo.write(registro)
            print("Saque realizado e registrado no extrato.")
        except Exception as e:
            print(f"Erro ao tentar salvar o extrato: {e}")
        
        return self._saldo
    
    def mostrar_extrato(self):
        try:
            # Abre o arquivo extrato.txt em modo de leitura
            with open('C:\\Users\\cau-humberto\\Documents\\GitHub\\Teste_code\\POO\\Banco\\extrato.txt', 'r') as arquivo:
                # Lê todo o conteúdo do arquivo
                conteudo = arquivo.readlines()
                
                # Verifica se o arquivo está vazio
                if not conteudo:
                    print("Não há registros no extrato.")
                else:
                    # Exibe cada linha do extrato
                    print("Extrato de Transações:")
                    for linha in conteudo:
                        print(linha.strip())  # strip() remove espaços em branco e quebras de linha desnecessárias
        except FileNotFoundError:
            print("O arquivo extrato.txt não foi encontrado. Nenhum extrato disponível.")
        except Exception as e:
            print(f"Ocorreu um erro ao tentar ler o extrato: {e}")

