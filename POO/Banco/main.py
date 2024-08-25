from conta import Conta
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca


def main():
    # conta = Conta('', '', '')

    # while True:
    #         try:
    #             print('-='*30)
    #             print('-------  BANCO  ---------')
    #             print('TOPA TUDO POR DINHEIRO')
    #             print('''
    #             1 - Cadastrar Conta
    #             2 - Ver Saldo
    #             3 - Depositar
    #             4 - Sacar
    #             5 - Extrato
    #             6 - Validar Senha
    #             7 - Trocar Senha
    #             8 - SAIR
    #             ''')
    #             print('-='*30)
    #             res = int(input('Digite uma Opção: '))
                
    #             if res == 1:
    #                 conta.cadastrar_conta()
                
    #             elif res == 2:
    #                 print('Saldo da Conta:')
    #                 conta.mostrar_saldo()
    #                 print('-='*30)

    #             elif res == 3:
    #                 print('Deposito:')
    #                 conta.depositar()
    #                 print('-='*30)
                
    #             elif res == 4:
    #                 print('Sacar:')
    #                 conta.sacar()
    #                 print('-='*30)

    #             elif res == 5:
    #                 print('Extrato:')
    #                 conta.extrato()
    #                 print('-='*30)

    #             elif res == 6:
    #                 print('Validar Senha:')
    #                 conta.validar_senha()
    #                 print('-='*30)

    #             elif res == 7:
    #                 print('Mudar a Senha:')
    #                 conta.trocar_senha()
    #                 print('-='*30)
                
    #             elif res == 8:
    #                 print('Encerrando Operações...')
    #                 break
                
    #             else:
    #                 print('\033[1;31;41mOpção inválida. Tente novamente.\033[m')
    #         except ValueError:
    #             print('\033[1;31;41mO valor Digitado não é um número\033[m')

    print('-='*40)
    print('Conta:')

    conta = Conta('Humberto', 1000, 111)
    print(f'Titular: {conta.titular} \nSaldo: {conta._saldo}')
    #conta.sacar()
    #print(f'Titular: {conta.titular} \nSaldo: {conta._saldo}')

    print('-='*40)
    print('Conta Corrente:')
    contaCorrente = ContaCorrente('Alcantara', 111, 2000, 5000)
    print(contaCorrente.detalhar_conta())


    print('-='*40)
    print('Conta Poupança:')
    contaPoupanca = ContaPoupanca('Junior', 111, 10000)
    print(f'Titular: {contaPoupanca.titular} \nSaldo: {contaPoupanca._saldo}')


main()
