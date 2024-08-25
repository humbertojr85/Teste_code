from POO.Banco.conta import Conta


def main():
    conta = Conta('', '', '')

    while True:
            try:
                print('-='*30)
                print('-------  BANCO  ---------')
                print('TOPA TUDO POR DINHEIRO')
                print('''
                1 - Cadastrar Conta
                2 - Ver Saldo
                3 - Depositar
                4 - Sacar
                5 - Extrato
                6 - Validar Senha
                7 - Trocar Senha
                8 - SAIR
                ''')
                print('-='*30)
                res = int(input('Digite uma Opção: '))
                
                if res == 1:
                    conta.cadastrar_conta()
                
                elif res == 2:
                    print('Saldo da Conta:')
                    conta.mostrar_saldo()
                    print('-='*30)

                elif res == 3:
                    print('Deposito:')
                    conta.depositar()
                    print('-='*30)
                
                elif res == 4:
                    print('Sacar:')
                    conta.sacar()
                    print('-='*30)

                elif res == 5:
                    print('Extrato:')
                    conta.extrato()
                    print('-='*30)

                elif res == 6:
                    print('Validar Senha:')
                    conta.validar_senha()
                    print('-='*30)

                elif res == 7:
                    print('Mudar a Senha:')
                    conta.trocar_senha()
                    print('-='*30)
                
                elif res == 8:
                    print('Encerrando Operações...')
                    break
                
                else:
                    print('\033[1;31;41mOpção inválida. Tente novamente.\033[m')
            except ValueError:
                print('\033[1;31;41mO valor Digitado não é um número\033[m')

main()
