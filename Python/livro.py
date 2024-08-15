class Livro():
    def __init__(self, titulo, autor, ano, editora='Não informado'):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editora = editora
    
    def listar_livros(self):
        return [self.titulo, self.autor, self.ano, self.editora]
    
########################################################################
#Outra classe

class Biblioteca:
    def __init__(self, nome_biblioteca):
        self.nome_biblioteca = nome_biblioteca
        self.livros = []
        self.livros_alugados = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def mostrar_livros(self):
        return [livro.listar_livros() for livro in self.livros]
    
    def cadastrar_livro(self, titulo, autor, ano, editora='Não informado'):
        novo_livro = Livro(titulo, autor, ano, editora)
        self.adicionar_livro(novo_livro)

    def exibir_livros(self):
        for livro in self.mostrar_livros():
            print(f"Título: {livro[0]}")
            print(f"Autor: {livro[1]}")
            print(f"Ano: {livro[2]}")
            print(f"Editora: {livro[3]}")
            print("-" * 30)  # Separador entre os livros

    def resumo(self):
        nomes_livros = ', '.join([livro[0] for livro in self.mostrar_livros()])
        return f'Biblioteca: {self.nome_biblioteca}\nLivros: {nomes_livros}'

    def alugar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                self.livros_alugados.append(livro)
                print(f'\033[1;36;40mVocê alugou o livro "{titulo}".\033[m')
                return
        print(f'O livro "{titulo}" não está disponível para aluguel.')

    def devolver_livro(self, titulo):
        for livro in self.livros_alugados:
            if livro.titulo == titulo:
                self.livros_alugados.remove(livro)
                self.adicionar_livro(livro)
                print(f'\033[1;36;40mVocê devolveu o livro "{titulo}".\033[m')
                return
        print(f'O livro "{titulo}" não foi encontrado entre os livros alugados.')