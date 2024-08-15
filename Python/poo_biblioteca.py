from livro import Livro
from livro import Biblioteca

def main():
    biblioteca = Biblioteca('Biblioteca Conhecimento Nunca é D+')

    while True:
        try:
            print('-='*30)
            print('-------  MENU DE OPÇÕES  ---------')
            print('BIBLIOTECA CONHECIMENTO NUNCA É D+')
            print('''
            1 - Cadastrar Livro
            2 - Mostrar Livros
            3 - Alugar Livro
            4 - Devolver Livro
            5 - SAIR
            ''')
            print('-='*30)
            res = int(input('Digite uma Opção: '))
            
            if res == 1:
                titulo = input('Digite o título do livro: ')
                autor = input('Digite o autor do livro: ')
                ano = int(input('Digite o ano de publicação: '))
                editora = input('Digite a editora do livro (ou pressione Enter para "Não informado"): ')
                if not editora:
                    editora = 'Não informado'
                biblioteca.cadastrar_livro(titulo, autor, ano, editora)
                print('Livro cadastrado com sucesso!')
            
            elif res == 2:
                print('Mostrando todos os livros cadastrados:')
                print(biblioteca.resumo())
                print('-='*30)
                biblioteca.exibir_livros()

            elif res == 3:
                titulo = input('Digite o título do livro que deseja alugar: ')
                biblioteca.alugar_livro(titulo)
            
            elif res == 4:
                titulo = input('Digite o título do livro que deseja devolver: ')
                biblioteca.devolver_livro(titulo)
            
            elif res == 5:
                print('Saindo do programa')
                break
            
            else:
                print('\033[1;31;41mOpção inválida. Tente novamente.\033[m')
        except ValueError:
            print('\033[1;31;41mO valor Digitado não é um número\033[m')

main()

