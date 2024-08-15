from livro import Livro

class Biblioteca:
    def __init__(self, nome_biblioteca):
        self.nome_biblioteca = nome_biblioteca
        self.livros = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def mostrar_livros(self):
        return [livro.listar_livros() for livro in self.livros]
    
    def cadastrar_livro(self, titulo, autor, ano, editora='Não informado'):
        novo_livro = Livro(titulo, autor, ano, editora)
        self.adicionar_livro(novo_livro)

    def exibir_livros(self):
        # Exibir todos os livros cadastrados com todas as informações
        for livro in self.mostrar_livros():
            print(f"Título: {livro[0]}")
            print(f"Autor: {livro[1]}")
            print(f"Ano: {livro[2]}")
            print(f"Editora: {livro[3]}")
            print("-" * 30)  # Separador entre os livros

    def resumo(self):
        nomes_livros = ', '.join([livro[0] for livro in self.mostrar_livros()])
        return f'Biblioteca: {self.nome_biblioteca}\nLivros: {nomes_livros}'

def main():
    biblioteca = Biblioteca('Biblioteca Conhecimento Nunca é D+')

    while True:
        print('-='*30)
        print('OPÇÕES DA BIBLIOTECA')
        print('''
        1 - Cadastrar Livro
        2 - Mostrar Livros
        3 - SAIR
        ''')
        print('-='*30)
        res = int(input('Digite uma Opção: '))
        
        if res == 1:
            # Pedir ao usuário para inserir os detalhes do livro
            titulo = input('Digite o título do livro: ')
            autor = input('Digite o autor do livro: ')
            ano = int(input('Digite o ano de publicação: '))
            editora = input('Digite a editora do livro (ou pressione Enter para "Não informado"): ')
            
            # Se o usuário não fornecer uma editora, usar "Não informado"
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
            print('Saindo do programa')
            break
        
        else:
            print('Opção inválida. Tente novamente.')


main()
